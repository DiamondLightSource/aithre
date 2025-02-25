#!.venv/bin/python
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
# import rtc6_fastcs
# import rtc6_fastcs.cut_shapes
# import rtc6_fastcs.plan_stubs
from control import ca
import pv
import math
import numpy as np
import time
import os
from guiv4_2_6beta import Ui_MainWindow
from datetime import datetime
import zmq
import pickle
import asyncio
import laserControl as lc
import httpx
from qasync import QEventLoop


version = "4.2.6"
OAVADDRESS = "http://bl23i-ea-serv-01.diamond.ac.uk:8080/OAV.mjpg.mjpg"
LASERENDPOINT = "http://172.23.17.123:20010"
# Set grid/beam position/scale.
line_width = 2
line_spacing = 115  # depends on pixel size, 60 for MANTA507B
line_color = (140, 140, 140)  # greyness
beamX = 2210
beamY = 1186
feed_width = int(ca.caget(pv.oav_max_x))
display_width = 2012  # 2012
display_height = 1528  # 1518
camera_pixel_size = 1.85  # Alvium1240M
feed_display_ratio = feed_width / display_width
calibrate = (
    camera_pixel_size / feed_display_ratio
) / 1000  # play around with the end number to find correct

print(
    f"Feed to display ratio is {str(feed_display_ratio)} so calibrate value for pixel size of {str(camera_pixel_size)}um should be {str(calibrate)}"
)


# separate thread for OAV
class OAVThread(QtCore.QThread):
    ImageUpdate = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self):
        super(OAVThread, self).__init__()
        self.ThreadActive = False
        self.zoomLevel = 1
        self.beamX = beamX
        self.beamY = beamY
        self.line_width = line_width
        self.line_spacing = line_spacing
        self.line_color = line_color

    def run(self):
        self.ThreadActive = True
        self.cap = cv.VideoCapture(OAVADDRESS)
        while self.ThreadActive:
            ret, frame = self.cap.read()
            if self.ThreadActive and ret:
                for i in range(beamX % line_spacing, frame.shape[1], line_spacing):
                    cv.line(frame, (i, 0), (i, frame.shape[0]), line_color, line_width)
                for i in range(beamY % line_spacing, frame.shape[0], line_spacing):
                    cv.line(frame, (0, i), (frame.shape[1], i), line_color, line_width)

                cv.line(
                    frame,
                    (beamX - 20, beamY),  # bigness
                    (beamX + 20, beamY),
                    (0, 255, 0),  # color
                    3,  # thickness
                )
                cv.line(
                    frame,
                    (beamX, beamY - 20),
                    (beamX, beamY + 20),
                    (0, 255, 0),
                    3,
                )

                if self.zoomLevel != 1:
                    new_width = int(frame.shape[1] / self.zoomLevel)
                    new_height = int(frame.shape[0] / self.zoomLevel)

                    x1 = max(self.beamX - new_width // 2, 0)
                    y1 = max(self.beamY - new_height // 2, 0)
                    x2 = min(self.beamX + new_width // 2, frame.shape[1])
                    y2 = min(self.beamY + new_height // 2, frame.shape[0])

                    x1, x2 = self.adjust_roi_boundaries(
                        x1, x2, frame.shape[1], new_width
                    )
                    y1, y2 = self.adjust_roi_boundaries(
                        y1, y2, frame.shape[0], new_height
                    )

                    cropped_frame = frame[y1:y2, x1:x2]

                    frame = cv.resize(cropped_frame, (frame.shape[1], frame.shape[0]))

                rgbImage = cv.cvtColor(
                    frame, cv.COLOR_BGR2RGB
                )  
                convertToQtFormat = QtGui.QImage(
                    rgbImage.data,
                    rgbImage.shape[1],
                    rgbImage.shape[0],
                    QtGui.QImage.Format_RGB888,
                )
                p = convertToQtFormat
                p = convertToQtFormat.scaled(
                    display_width, display_height, QtCore.Qt.KeepAspectRatio
                ) 
                self.ImageUpdate.emit(p)

    def adjust_roi_boundaries(self, start, end, max_value, window_size):
        if start < 0:
            end -= start
            start = 0
        if end > max_value:
            start -= end - max_value
            end = max_value
        if (end - start) < window_size and (start + window_size) <= max_value:
            end = start + window_size
        return start, end

    def setZoomLevel(self, zoomLevel):
        self.zoomLevel = zoomLevel

    def stop(self):
        self.ThreadActive = False
        self.cap.release()


# separate thread to run caget for RBVs
class RBVThread(QtCore.QThread):
    rbvUpdate = QtCore.pyqtSignal(list)

    def run(self):
        while True:
            time.sleep(1)
            allRBVsList = []
            allRBVsList += [str(ca.caget(pv.stage_x_rbv))]
            allRBVsList += [str(ca.caget(pv.gonio_y_rbv))]
            allRBVsList += [str(ca.caget(pv.gonio_z_rbv))]
            allRBVsList += [str(ca.caget(pv.omega_rbv))]
            allRBVsList += [str(ca.caget(pv.oav_cam_acqtime_rbv))]
            allRBVsList += [str(ca.caget(pv.oav_cam_gain_rbv))]
            allRBVsList += [str(ca.caget(pv.robot_current_pin_rbv))]
            if (
                ca.caget(pv.robot_pin_mounted) is True
            ):  # need to work out what this pv returns
                allRBVsList += "\u2714"
            elif ca.caget(pv.robot_pin_mounted) is False:
                allRBVsList += "\u274C"
            else:
                allRBVsList += "\u003F"
            allRBVsList += [str(ca.caget(pv.stage_z_rbv))]
            allRBVsList += [str(ca.caget(pv.stage_y_rbv))]
            self.rbvUpdate.emit(allRBVsList)
            # print(f"lRBVThreadComplete {str(datetime.now())}")


class LaserStatusThread(QtCore.QThread):
    statusUpdate = QtCore.pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.endpoint = LASERENDPOINT
        self.interval = 500
        self._is_running = True
        self.endpoints = {
            "IsOutputEnabled": f"{self.endpoint}/v1/Basic/IsOutputEnabled",
            "ActualShutterState": f"{self.endpoint}/v1/Basic/ActualShutterState",
            "ActualOutputFrequency": f"{self.endpoint}/v1/Basic/ActualOutputFrequency",
            "ActualAttenuatorPercentage": f"{self.endpoint}/v1/Basic/ActualAttenuatorPercentage",
            "ActualPpDivider": f"{self.endpoint}/v1/Basic/ActualPpDivider",
            "ActualStateName": f"{self.endpoint}/v1/Basic/ActualStateName",
        }

    async def fetchStatus(self):
        async with httpx.AsyncClient(timeout=10.0) as client:
            tasks = []
            for name, url in self.endpoints.items():
                tasks.append(self.fetchEndpoint(client, name, url))
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return dict(results)

    async def fetchEndpoint(self, client, name, url):
        try:
            response = await client.get(url)
            if response.status_code == 200:
                return (name, response.text.strip())
            return (name, f"Error: {response.status_code}")
        except Exception as e:
            return (name, f"Error: {str(e)}")

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        while self._is_running:
            try:
                status_dict = loop.run_until_complete(self.fetchStatus())
                self.statusUpdate.emit(status_dict)
            except Exception as e:
                print(f"Error fetching status: {str(e)}")
            QtCore.QThread.msleep(self.interval)

    def stop(self):
        self._is_running = False


# class robotCheckThread(QtCore.QThread):
#     robotUpdate = QtCore.pyqtSignal(list)

#     def run(self):
#         while True:
#             time.sleep(1)
#             robotUpdateList = []
#             robotUpdateList += [str(ca.caget(pv.robot_prog_running))]
#             self.robotUpdate.emit(robotUpdateList)


# class beamlineSafeThread(QtCore.QThread):
#     beamlineSafe = QtCore.pyqtSignal(list)

#     def run(self):
#         self.ThreadActive = True
#         while self.ThreadActive:
#             safeUpdateList = []
#             safeUpdateList += [str(ca.caget(pv.stage_x_rbv))]
#             safeUpdateList += [str(ca.caget(pv.gonio_y_rbv))]
#             safeUpdateList += [str(ca.caget(pv.gonio_z_rbv))]
#             safeUpdateList += [str(ca.caget(pv.omega_rbv))]
#             safeUpdateList += [str(ca.caget(pv.stage_z_rbv))]
#             safeUpdateList += [str(ca.caget(pv.stage_y_rbv))]
#             blsafe = all(round(float(safeUpdateList[x]), 3) == 0.00 for x in [0, 1, 2, 3, 4, 5])
#             if blsafe:
#                 safeUpdateList = ["Yes"]
#             else:
#                 safeUpdateList = ["No"]
#             self.beamlineSafe.emit(safeUpdateList)


class MainWindow(QtWidgets.QMainWindow):
    zoomChanged = QtCore.pyqtSignal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.drawn_points = []
        #self.rtc6 = rtc6_fastcs.cut_shapes.CutShapes()

        # menus
        self.ui.actionExit.triggered.connect(self.quit)
        # sliders and sensors
        self.ui.sliderExposure.setProperty(
            "value", str(round(float(ca.caget(pv.oav_cam_acqtime_rbv)) * 100))
        )
        self.ui.sliderGain.setProperty(
            "value", str(round(float(ca.caget(pv.oav_cam_gain_rbv))))
        )
        # OAV zoom setup
        self.ui.sliderZoom.valueChanged.connect(self.handleZoom)
        # OAV connections thread
        self.zoomLevel = 1
        self.setupOAV()
        self.OAVth = OAVThread()
        self.OAVth.ImageUpdate.connect(self.setImage)
        self.OAVth.start()
        self.zoomChanged.connect(self.OAVth.setZoomLevel)
        self.canvasMode = "move"
        self.ui.oav_stream.mousePressEvent = self.onMouse
        self.ui.start.clicked.connect(self.oavStart)
        self.ui.stop.clicked.connect(self.oavStop)
        self.ui.snapshot.clicked.connect(self.saveSnapshot)
        self.ui.AutoCenter.clicked.connect(self.autoCenter)
        # RBV updating connections thread
        RBVth = RBVThread()
        RBVth.rbvUpdate.connect(self.updateRBVs)
        RBVth.start()
        # robot active thread
        # th3 = robotCheckThread()
        # th3.robotUpdate.connect(self.setRobotActiveStatus)
        # th3.start()
        # th4 = beamlineSafeThread()
        # th4.beamlineSafe.connect(self.beamlineSafeStatus)
        # th4.start()
        # gonio rotation buttons
        self.ui.buttonSlowOmegaTurn.clicked.connect(lambda: ca.caput(pv.omega_velo, 15))
        self.ui.buttonFastOmegaTurn.clicked.connect(lambda: ca.caput(pv.omega_velo, 40))
        self.ui.plusMinus3600.clicked.connect(self.goTopm3600)
        self.ui.minus180.clicked.connect(lambda: self.gonioRotate(-180))
        self.ui.plus180.clicked.connect(lambda: self.gonioRotate(180))
        self.ui.minus90.clicked.connect(lambda: self.gonioRotate(-90))
        self.ui.plus90.clicked.connect(lambda: self.gonioRotate(90))
        self.ui.minus15.clicked.connect(lambda: self.gonioRotate(-15))
        self.ui.plus15.clicked.connect(lambda: self.gonioRotate(15))
        self.ui.minus5.clicked.connect(lambda: self.gonioRotate(-5))
        self.ui.plus5.clicked.connect(lambda: self.gonioRotate(5))
        self.ui.zero.clicked.connect(lambda: self.gonioRotate(0))
        # jog buttons
        self.ui.up.clicked.connect(lambda: self.jogSample("up"))
        self.ui.down.clicked.connect(lambda: self.jogSample("down"))
        self.ui.left.clicked.connect(lambda: self.jogSample("left"))
        self.ui.right.clicked.connect(lambda: self.jogSample("right"))
        self.ui.pushButtonZMinus.clicked.connect(lambda: self.jogSample("ZMinus"))
        self.ui.pushButtonZPlus.clicked.connect(lambda: self.jogSample("ZPlus"))
        # exposure and gain sliders
        self.ui.sliderExposure.valueChanged.connect(self.changeExposureGain)
        self.ui.sliderGain.valueChanged.connect(self.changeExposureGain)
        self.ui.zeroAll.clicked.connect(self.returntozero)
        # robot buttons
        self.ui.resetRobot.clicked.connect(lambda: ca.caput(pv.robot_reset, 1))
        self.ui.load.clicked.connect(self.loadNextPin)
        self.ui.unload.clicked.connect(self.unloadPin)
        self.ui.dry.clicked.connect(self.dryGripper)
        # zoom_level = self.ui.sliderZoom.value()
        # laser buttons
        self.ui.pushButtonDisableLaser.clicked.connect(lambda: self.commandLaser("Disable"))
        self.ui.pushButtonEnableLaser.clicked.connect(lambda: self.commandLaser("Enable"))
        self.ui.pushButtonSetDivider.clicked.connect(lambda: self.commandLaser("SetDivider"))
        self.ui.pushButtonSetAttenuator.clicked.connect(lambda: self.commandLaser("SetAttenuator"))
        self.ui.pushButtonStartupLaser.clicked.connect(lambda: self.commandLaser("Startup"))
        self.ui.pushButtonStandbyLaser.clicked.connect(lambda: self.commandLaser("Standby"))
        # move/draw options
        self.ui.radioButtonMoveMode.toggled.connect(lambda: self.toggleCanvasMode("move"))
        self.ui.radioButtonDrawMode.toggled.connect(lambda: self.toggleCanvasMode("draw"))
        self.ui.pushButtonClear.clicked.connect(lambda: self.drawn_points.clear())
        self.ui.pushButtonCut.clicked.connect(self.savePoints)

        self.laserStatusThread = LaserStatusThread()
        self.laserStatusThread.statusUpdate.connect(self.updateLaserStatus)
        self.laserStatusThread.start()

    def updateLaserStatus(self, status_dict):
        if status_dict["IsOutputEnabled"] == "true":
            self.ui.labOUTPUT.setStyleSheet("background-color: green")
        else:
            self.ui.labOUTPUT.setStyleSheet("background-color: red")

        if status_dict["ActualShutterState"] == '"Opened"':
            self.ui.labEMISSION.setStyleSheet("background-color: green")
        elif status_dict["ActualShutterState"] == '"Closed"':
            self.ui.labEMISSION.setStyleSheet("background-color: red")
        else:
            self.ui.labEMISSION.setStyleSheet("background-color: yellow")

        self.outputDivider = status_dict["ActualPpDivider"]
        self.outputFrequency = status_dict["ActualOutputFrequency"]
        self.DivFreq = f"{(self.outputDivider)} / {str(np.round(float(self.outputFrequency), 2))} Hz"
        self.ui.labDividerRBV.setText(self.DivFreq)
        self.outputAttenuator = status_dict["ActualAttenuatorPercentage"]
        self.ui.labAttenuatorRBV.setText(str(np.round(float(self.outputAttenuator), 1)))
        self.ui.labLaserStatus.setText(status_dict["ActualStateName"])

    def closeEvent(self, event):
        self.laserStatusThread.stop()
        self.laserStatusThread.quit()
        self.laserStatusThread.wait()
        event.accept()

    def commandLaser(self, command):
        laser = lc.carbide(endpoint=LASERENDPOINT)
        if command == "Enable":
            laser.changeOutput(state="enable")
        elif command == "Disable":
            laser.changeOutput(state="close")
        elif command == "SetDivider":
            laser.setPpDivider(divider=int(self.ui.spinBoxDivider.value()))
        elif command == "SetAttenuator":
            laser.setAttenuatorPercentage(percentage=float(self.ui.doubleSpinBoxAttenuator.value()))
        elif command == "Startup":
            laser.selectAndApplyPreset(preset="5")
        elif command == "Standby":
            laser.goToStandby()


    def loadNextPin(self):
        ca.caput(pv.robot_reset, 1)
        time.sleep(3)
        ca.caput(pv.robot_next_pin, int(self.ui.spinToLoad.value()))
        time.sleep(3)
        ca.caput(pv.robot_proc_load, 1)

    def unloadPin(self):
        ca.caput(pv.robot_reset, 1)
        time.sleep(3)
        ca.caput(pv.robot_proc_unload, 1)

    def dryGripper(self):
        ca.caput(pv.robot_reset, 1)
        time.sleep(3)
        ca.caput(pv.robot_proc_dry, 1)

    def quit(self):
        sys.exit()

    def returntozero(self):
        for motor in [pv.gonio_y, pv.gonio_z, pv.stage_x, pv.omega]:
            ca.caput(motor, 0)

    def handleZoom(self, zoomValue):
        self.zoomLevel = zoomValue
        self.ui.currentZoom.setText(str(self.zoomLevel))
        self.zoomChanged.emit(self.zoomLevel)

    def changeExposureGain(self):
        ca.caput(pv.oav_cam_acqtime, (self.ui.sliderExposure.value() / 100))
        ca.caput(pv.oav_cam_gain, self.ui.sliderGain.value())

    def jogSample(self, direction):
        if direction == "right":
            ca.caput(pv.stage_x, (float(ca.caget(pv.stage_x_rbv)) + 0.005))
        elif direction == "left":
            ca.caput(pv.stage_x, (float(ca.caget(pv.stage_x_rbv)) - 0.005))
        elif direction == "up":
            ca.caput(
                pv.gonio_y,
                (float(ca.caget(pv.gonio_y_rbv)))
                + ((math.sin(math.radians(float(ca.caget(pv.omega_rbv)))))) * 0.005,
            )
            ca.caput(
                pv.gonio_z,
                (float(ca.caget(pv.gonio_z_rbv)))
                + ((math.cos(math.radians(float(ca.caget(pv.omega_rbv)))))) * 0.005,
            )
        elif direction == "down":
            ca.caput(
                pv.gonio_y,
                (float(ca.caget(pv.gonio_y_rbv)))
                - ((math.sin(math.radians(float(ca.caget(pv.omega_rbv)))))) * 0.005,
            )
            ca.caput(
                pv.gonio_z,
                (float(ca.caget(pv.gonio_z_rbv)))
                - ((math.cos(math.radians(float(ca.caget(pv.omega_rbv)))))) * 0.005,
            )
        elif direction == "ZPlus":
            ca.caput(pv.stage_z, (float(ca.caget(pv.stage_z_rbv)) + 0.05))
        elif direction == "ZMinus":
            ca.caput(pv.stage_z, (float(ca.caget(pv.stage_z_rbv)) - 0.05))
        else:
            pass

    def goTopm3600(self):
        gonio_current = float(ca.caget(pv.omega_rbv))
        if gonio_current <= 0:
            gonio_request = 3600
        else:
            gonio_request = -3600
        print("Moving gonio omega to", str(gonio_request))
        ca.caput(pv.omega, gonio_request)

    def toggleCanvasMode(self, mode):
        if mode == "move":
            self.canvasMode = "move"
        elif mode == "draw":
            self.canvasMode = "draw"
        else:
            self.canvasMode = "move"

    def onMouse(self, event):
        if self.canvasMode == "move":
            x = event.pos().x()
            x = x * feed_display_ratio
            y = event.pos().y()
            y = y * feed_display_ratio
            x_curr = float(ca.caget(pv.stage_x_rbv))
            #print(x_curr)
            y_curr = float(ca.caget(pv.gonio_y_rbv))
            z_curr = float(ca.caget(pv.gonio_z_rbv))
            omega = float(ca.caget(pv.omega_rbv))
            #print("Clicked", x, y)
            Xmove = x_curr - ((x - beamX) * calibrate)
            #print((x - beamX))
            Ymove = y_curr + (math.sin(math.radians(omega)) * ((y - beamY) * calibrate))
            Zmove = z_curr + (math.cos(math.radians(omega)) * ((y - beamY) * calibrate))
            print("Moving", Xmove, Ymove, Zmove)
            ca.caput(pv.stage_x, Xmove)
            ca.caput(pv.gonio_y, Ymove)
            ca.caput(pv.gonio_z, Zmove)
        elif self.canvasMode == "draw":
            self.drawn_points.append(event.pos())
            self.redrawPoints()
        else:
            pass
        
    def redrawPoints(self):
        if self.image is not None:
            painter = QtGui.QPainter(self.image)
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 5))
            if len(self.drawn_points) < 2:
                for point in self.drawn_points:
                    painter.drawPoint(point)
            if len(self.drawn_points) > 1:
                for i in range(len(self.drawn_points) - 1):
                    painter.drawLine(self.drawn_points[i], self.drawn_points[i + 1])
            painter.end()
            self.ui.oav_stream.setPixmap(QtGui.QPixmap.fromImage(self.image))

    def savePoints(self):
        points_list = []
        now = datetime.now()
        filename = now.strftime("%Y%m%d_%H%M%S_points.txt")
        for i, point in enumerate(self.drawn_points):
            correctedX = point.x() * calibrate
            correctedY = point.y() * calibrate
            if i == 0:
                points_list.append((correctedX, correctedY, False))
            else:
                points_list.append((correctedX, correctedY, True))
        for point in self.drawn_points:
            correctedX = point.x() * calibrate
            correctedY = point.y() * calibrate
        with open(filename, 'w') as file:
            file.write(f"{correctedX}, {correctedY}\n")
        

        #scanhead = rtc6_fastcs.cut_shapes.CutShapes()

        
                    
    def setupOAV(self):
        for callback in (
            pv.oav_roi_ecb,
            pv.oav_arr_ecb,
            pv.oav_stat_ecb,
            pv.oav_proc_ecb,
            pv.oav_over_ecb,
            pv.oav_fimg_ecb,
            pv.oav_tiff_ecb,
            pv.oav_hdf5_ecb,
            pv.oav_pva_ecb,
        ):
            ca.caput(callback, "Disable")
        ca.caput(pv.oav_mjpg_maxw, 4024)
        ca.caput(pv.oav_mjpg_maxh, 3036)

    def oavStart(self):
        ca.caput(pv.oav_acquire, "Acquire")

    def oavStop(self):
        ca.caput(pv.oav_acquire, "Done")

    def setImage(self, image):
        self.image = image
        self.redrawPoints()
        self.ui.oav_stream.setPixmap(QtGui.QPixmap.fromImage(image))

    def saveSnapshot(self):
        image = self.image
        print(f"Q image format: {image.format()}")
        print(f"Q image bytes: {image.byteCount()}")
        print(f"Q image bytes per line: {image.bytesPerLine()}")
        width = image.width()
        height = image.height()
        bytesPerLine = image.bytesPerLine()
        data = image.bits().asstring(height * bytesPerLine)
        arr = np.frombuffer(data, dtype=np.uint8).reshape((height, width, 3))
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.ui.centralwidget,
            "QFileDialog.getSaveFileName()",
            "",
            "JPEG Files (*.jpg);;All Files (*)",
            options=options,
        )

        if file_name:
            _, file_extension = os.path.splitext(file_name)
            if not file_extension:
                file_name += ".jpg"
            try:
                result = cv.imwrite(file_name, arr)
                if result:
                    print("Image saved successfully.")
                else:
                    print("Failed to save image. Try as a .jpg")
            except Exception as e:
                print(f"An error occurred while saving the image: {e}")

    def gonioRotate(self, amount):
        gonio_current = float(ca.caget(pv.omega_rbv))
        if amount == 0:
            gonio_request = 0
        else:
            gonio_request = gonio_current + amount
        print("Moving gonio omega to", str(gonio_request))
        ca.caput(pv.omega, gonio_request)

    def updateRBVs(self, rbvs):
        # stagez, gony, gonz, omega, oavexp, oavgain, currentsamp, goniosens, stagex, stagey
        self.ui.stagez_rbv.setText(
            str(round(float(rbvs[0]), 3))
        )  # used to be x now is z
        self.ui.gony_rbv.setText(str(round(float(rbvs[1]), 3)))
        self.ui.gonz_rbv.setText(str(round(float(rbvs[2]), 3)))
        # stop -0.0 to 0.0 jitter on GUI
        if round(float(rbvs[3]), 0) == -0.0:
            self.ui.omega_rbv.setText("0.0")
        else:
            self.ui.omega_rbv.setText(str(round(float(rbvs[3]), 0)))
        self.ui.exposure_rbv.setText(str(round(float(rbvs[4]), 3)))
        self.ui.gain_rbv.setText(str(int(rbvs[5])))
        self.ui.currentSamp.setText(str(rbvs[6]))
        blsafe = all(round(float(rbvs[x]), 3) == 0.00 for x in [0, 1, 2, 3, 8, 9])
        if blsafe:
            ca.caput(pv.robot_ip16_force_option, "On")
            self.ui.indicatorBeamlineSafe.setStyleSheet("background-color: green")
        else:
            # ca.caput(pv.robot_ip16_force_option, "No")
            self.ui.indicatorBeamlineSafe.setStyleSheet("background-color: red")
        if ca.caget(pv.robot_pin_mounted) == "Yes":
            self.ui.indicatorGonioSensor.setStyleSheet("background-color: green")
        else:
            self.ui.indicatorGonioSensor.setStyleSheet("background-color: red")

    # def setRobotActiveStatus(self, robotUpdateList):
    #     if str(robotUpdateList[0]) == "No":
    #         self.ui.indicatorRobotActive.setStyleSheet("background-color: red")
    #     else:
    #         self.ui.indicatorRobotActive.setStyleSheet("background-color: green")
            # ca.caput(
            #     pv.gonio_y,
            #     (float(ca.caget(pv.gonio_y_rbv)))
            #     - ((math.cos(math.radians(float(ca.caget(pv.omega_rbv)))))) * 0.05,
            # )
            # ca.caput(
            #     pv.gonio_z,
            #     (float(ca.caget(pv.gonio_z_rbv)))
            #     - ((math.sin(math.radians(float(ca.caget(pv.omega_rbv)))))) * 0.05,
            # )lf, beamlineSafeList):
    #     if str(beamlineSafeList[0]) == "Yes":
    #         ca.caput(pv.robot_ip16_force_option, "On")
    #         self.ui.indicatorBeamlineSafe.setStyleSheet("background-color: green")
    #     elif str(beamlineSafeList[0]) == "No":
    #         ca.caput(pv.robot_ip16_force_option, "No")
    #         self.ui.indicatorBeamlineSafe.setStyleSheet("background-color: red")
    #     else:
    #         pass

    def autoCenter(self):
        cap = cv.VideoCapture(
            "http://bl23i-ea-serv-01.diamond.ac.uk:8080/OAV.mjpg.mjpg"
        )
        ret, frame = cap.read()
        if ret:
            filename = os.path.join(
                os.path.dirname(os.getcwd()),
                "captures",
                "autoCenter",
                f"{datetime.now().strftime('%d%m%y_%H%M%S')}.jpg",
            )
            try:
                cv.imwrite(filename, frame)
            except cv.error as e:
                print(f"Could not write image file: {e}")
        # check if murko running
        # send image to murko and get info
        try:
            request_arguments = {}
            request_arguments["to_predict"] = str(filename)
            # request_arguments["model_img_size"] = (display_height, display_width)
            request_arguments["save"] = True
            request_arguments["min_size"] = 64
            request_arguments["description"] = [
                "foreground",
                "crystal",
                "loop_inside",
                "loop",
                ["crystal", "loop"],
                ["crystal", "loop", "stem"],
            ]
            context = zmq.context()
            socket = context.socket(zmq.REQ)
            # socket.connect("http://bl23i-ea-serv-01.diamond.ac.uk:89011")
            socket.connect("tcp://localhost")
            socket.send(pickle.dumps(request_arguments))
            raw_predictions = socket.recv()
            predictions = pickle.load(raw_predictions)
            print("Prediction successfull")
        except:
            print("Could not predict")

        
        # move stage to center
        # rotate 90 and repeat


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)  # Create QEventLoop
    asyncio.set_event_loop(loop)
    mainWin = MainWindow()
    mainWin.show()
    with loop:
        loop.run_forever()
    sys.exit(app.exec_())
