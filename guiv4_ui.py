# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/vwg85559/aithre/guiv4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 847)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("/Users/vwg85559/aithre/icon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frameFineControl = QtWidgets.QFrame(self.centralwidget)
        self.frameFineControl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFineControl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameFineControl.setObjectName("frameFineControl")
        self.readback_grid = QtWidgets.QGridLayout(self.frameFineControl)
        self.readback_grid.setObjectName("readback_grid")
        self.gony_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.gony_rbv.setObjectName("gony_rbv")
        self.readback_grid.addWidget(self.gony_rbv, 4, 1, 1, 1)
        self.gain_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.gain_rbv.setObjectName("gain_rbv")
        self.readback_grid.addWidget(self.gain_rbv, 2, 1, 1, 1)
        self.exposure_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.exposure_rbv.setObjectName("exposure_rbv")
        self.readback_grid.addWidget(self.exposure_rbv, 1, 1, 1, 1)
        self.sliderGain = QtWidgets.QSlider(self.frameFineControl)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGain.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderGain.setTickInterval(5)
        self.sliderGain.setObjectName("sliderGain")
        self.readback_grid.addWidget(self.sliderGain, 2, 3, 1, 1)
        self.openOAVZoom = QtWidgets.QPushButton(self.frameFineControl)
        self.openOAVZoom.setObjectName("openOAVZoom")
        self.readback_grid.addWidget(self.openOAVZoom, 0, 1, 1, 3)
        self.sliderExposure = QtWidgets.QSlider(self.frameFineControl)
        self.sliderExposure.setMinimum(1)
        self.sliderExposure.setMaximum(100)
        self.sliderExposure.setProperty("value", 4)
        self.sliderExposure.setOrientation(QtCore.Qt.Horizontal)
        self.sliderExposure.setInvertedAppearance(False)
        self.sliderExposure.setInvertedControls(False)
        self.sliderExposure.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderExposure.setTickInterval(5)
        self.sliderExposure.setObjectName("sliderExposure")
        self.readback_grid.addWidget(self.sliderExposure, 1, 3, 1, 1)
        self.labY = QtWidgets.QLabel(self.frameFineControl)
        self.labY.setAlignment(QtCore.Qt.AlignCenter)
        self.labY.setObjectName("labY")
        self.readback_grid.addWidget(self.labY, 4, 0, 1, 1)
        self.omega_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.omega_rbv.setObjectName("omega_rbv")
        self.readback_grid.addWidget(self.omega_rbv, 7, 1, 1, 1)
        self.labOmega = QtWidgets.QLabel(self.frameFineControl)
        self.labOmega.setAlignment(QtCore.Qt.AlignCenter)
        self.labOmega.setObjectName("labOmega")
        self.readback_grid.addWidget(self.labOmega, 7, 0, 1, 1)
        self.labGain = QtWidgets.QLabel(self.frameFineControl)
        self.labGain.setObjectName("labGain")
        self.readback_grid.addWidget(self.labGain, 2, 0, 1, 1)
        self.stagez_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.stagez_request.setText("")
        self.stagez_request.setMaxLength(5)
        self.stagez_request.setObjectName("stagez_request")
        self.readback_grid.addWidget(self.stagez_request, 3, 3, 1, 1)
        self.gony_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.gony_request.setMaxLength(5)
        self.gony_request.setObjectName("gony_request")
        self.readback_grid.addWidget(self.gony_request, 4, 3, 1, 1)
        self.labstageZ = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labstageZ.sizePolicy().hasHeightForWidth())
        self.labstageZ.setSizePolicy(sizePolicy)
        self.labstageZ.setAlignment(QtCore.Qt.AlignCenter)
        self.labstageZ.setObjectName("labstageZ")
        self.readback_grid.addWidget(self.labstageZ, 3, 0, 1, 1)
        self.gonz_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.gonz_request.setMaxLength(5)
        self.gonz_request.setObjectName("gonz_request")
        self.readback_grid.addWidget(self.gonz_request, 5, 3, 1, 1)
        self.gonz_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.gonz_rbv.setObjectName("gonz_rbv")
        self.readback_grid.addWidget(self.gonz_rbv, 5, 1, 1, 1)
        self.labExposure = QtWidgets.QLabel(self.frameFineControl)
        self.labExposure.setObjectName("labExposure")
        self.readback_grid.addWidget(self.labExposure, 1, 0, 1, 1)
        self.omega_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.omega_request.setMaxLength(5)
        self.omega_request.setObjectName("omega_request")
        self.readback_grid.addWidget(self.omega_request, 7, 3, 1, 1)
        self.stagez_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.stagez_rbv.setObjectName("stagez_rbv")
        self.readback_grid.addWidget(self.stagez_rbv, 3, 1, 1, 1)
        self.labZ = QtWidgets.QLabel(self.frameFineControl)
        self.labZ.setAlignment(QtCore.Qt.AlignCenter)
        self.labZ.setObjectName("labZ")
        self.readback_grid.addWidget(self.labZ, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.frameFineControl, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.frameRobot = QtWidgets.QFrame(self.centralwidget)
        self.frameRobot.setAutoFillBackground(False)
        self.frameRobot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRobot.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameRobot.setLineWidth(1)
        self.frameRobot.setObjectName("frameRobot")
        self.robot_grid = QtWidgets.QGridLayout(self.frameRobot)
        self.robot_grid.setObjectName("robot_grid")
        self.unload = QtWidgets.QPushButton(self.frameRobot)
        self.unload.setObjectName("unload")
        self.robot_grid.addWidget(self.unload, 8, 0, 1, 1)
        self.load = QtWidgets.QPushButton(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy)
        self.load.setObjectName("load")
        self.robot_grid.addWidget(self.load, 7, 0, 1, 1)
        self.labBeamlineSafe = QtWidgets.QLabel(self.frameRobot)
        self.labBeamlineSafe.setAlignment(QtCore.Qt.AlignCenter)
        self.labBeamlineSafe.setObjectName("labBeamlineSafe")
        self.robot_grid.addWidget(self.labBeamlineSafe, 4, 0, 1, 1)
        self.labRobotIOC = QtWidgets.QLabel(self.frameRobot)
        self.labRobotIOC.setAlignment(QtCore.Qt.AlignCenter)
        self.labRobotIOC.setObjectName("labRobotIOC")
        self.robot_grid.addWidget(self.labRobotIOC, 10, 0, 1, 1)
        self.labZoomIOC = QtWidgets.QLabel(self.frameRobot)
        self.labZoomIOC.setAlignment(QtCore.Qt.AlignCenter)
        self.labZoomIOC.setObjectName("labZoomIOC")
        self.robot_grid.addWidget(self.labZoomIOC, 12, 0, 1, 1)
        self.indicatorMotionIOC = QtWidgets.QLabel(self.frameRobot)
        self.indicatorMotionIOC.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorMotionIOC.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorMotionIOC.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorMotionIOC.setText("")
        self.indicatorMotionIOC.setObjectName("indicatorMotionIOC")
        self.robot_grid.addWidget(self.indicatorMotionIOC, 9, 1, 1, 1)
        self.labOAVIOC = QtWidgets.QLabel(self.frameRobot)
        self.labOAVIOC.setAlignment(QtCore.Qt.AlignCenter)
        self.labOAVIOC.setObjectName("labOAVIOC")
        self.robot_grid.addWidget(self.labOAVIOC, 11, 0, 1, 1)
        self.indicatorBeamlineSafe = QtWidgets.QLabel(self.frameRobot)
        self.indicatorBeamlineSafe.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorBeamlineSafe.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorBeamlineSafe.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorBeamlineSafe.setText("")
        self.indicatorBeamlineSafe.setObjectName("indicatorBeamlineSafe")
        self.robot_grid.addWidget(self.indicatorBeamlineSafe, 4, 1, 1, 1)
        self.resetRobot = QtWidgets.QPushButton(self.frameRobot)
        self.resetRobot.setObjectName("resetRobot")
        self.robot_grid.addWidget(self.resetRobot, 6, 0, 1, 1)
        self.labRobotActive = QtWidgets.QLabel(self.frameRobot)
        self.labRobotActive.setAlignment(QtCore.Qt.AlignCenter)
        self.labRobotActive.setObjectName("labRobotActive")
        self.robot_grid.addWidget(self.labRobotActive, 5, 0, 1, 1)
        self.indicatorGonioSensor = QtWidgets.QLabel(self.frameRobot)
        self.indicatorGonioSensor.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorGonioSensor.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorGonioSensor.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorGonioSensor.setText("")
        self.indicatorGonioSensor.setScaledContents(False)
        self.indicatorGonioSensor.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.indicatorGonioSensor.setObjectName("indicatorGonioSensor")
        self.robot_grid.addWidget(self.indicatorGonioSensor, 1, 1, 1, 1)
        self.indicatorOAVIOC = QtWidgets.QLabel(self.frameRobot)
        self.indicatorOAVIOC.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorOAVIOC.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorOAVIOC.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorOAVIOC.setText("")
        self.indicatorOAVIOC.setObjectName("indicatorOAVIOC")
        self.robot_grid.addWidget(self.indicatorOAVIOC, 11, 1, 1, 1)
        self.labGonioSensor = QtWidgets.QLabel(self.frameRobot)
        self.labGonioSensor.setAlignment(QtCore.Qt.AlignCenter)
        self.labGonioSensor.setObjectName("labGonioSensor")
        self.robot_grid.addWidget(self.labGonioSensor, 1, 0, 1, 1)
        self.indicatorZoomIOC = QtWidgets.QLabel(self.frameRobot)
        self.indicatorZoomIOC.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorZoomIOC.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorZoomIOC.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorZoomIOC.setText("")
        self.indicatorZoomIOC.setObjectName("indicatorZoomIOC")
        self.robot_grid.addWidget(self.indicatorZoomIOC, 12, 1, 1, 1)
        self.goHomeRobot = QtWidgets.QPushButton(self.frameRobot)
        self.goHomeRobot.setObjectName("goHomeRobot")
        self.robot_grid.addWidget(self.goHomeRobot, 6, 1, 1, 1)
        self.indicatorRobotIOC = QtWidgets.QLabel(self.frameRobot)
        self.indicatorRobotIOC.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorRobotIOC.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorRobotIOC.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorRobotIOC.setText("")
        self.indicatorRobotIOC.setObjectName("indicatorRobotIOC")
        self.robot_grid.addWidget(self.indicatorRobotIOC, 10, 1, 1, 1)
        self.dry = QtWidgets.QPushButton(self.frameRobot)
        self.dry.setObjectName("dry")
        self.robot_grid.addWidget(self.dry, 8, 1, 1, 1)
        self.indicatorRobotActive = QtWidgets.QLabel(self.frameRobot)
        self.indicatorRobotActive.setMinimumSize(QtCore.QSize(20, 20))
        self.indicatorRobotActive.setMaximumSize(QtCore.QSize(20, 20))
        self.indicatorRobotActive.setFrameShape(QtWidgets.QFrame.Box)
        self.indicatorRobotActive.setText("")
        self.indicatorRobotActive.setObjectName("indicatorRobotActive")
        self.robot_grid.addWidget(self.indicatorRobotActive, 5, 1, 1, 1)
        self.spinToLoad = QtWidgets.QSpinBox(self.frameRobot)
        self.spinToLoad.setProperty("showGroupSeparator", False)
        self.spinToLoad.setMinimum(1)
        self.spinToLoad.setMaximum(16)
        self.spinToLoad.setObjectName("spinToLoad")
        self.robot_grid.addWidget(self.spinToLoad, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        self.robot_grid.addItem(spacerItem2, 3, 0, 1, 2)
        self.labCurrentSamp = QtWidgets.QLabel(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labCurrentSamp.sizePolicy().hasHeightForWidth()
        )
        self.labCurrentSamp.setSizePolicy(sizePolicy)
        self.labCurrentSamp.setAlignment(QtCore.Qt.AlignCenter)
        self.labCurrentSamp.setObjectName("labCurrentSamp")
        self.robot_grid.addWidget(self.labCurrentSamp, 0, 0, 1, 1)
        self.labMotionIOC = QtWidgets.QLabel(self.frameRobot)
        self.labMotionIOC.setAlignment(QtCore.Qt.AlignCenter)
        self.labMotionIOC.setObjectName("labMotionIOC")
        self.robot_grid.addWidget(self.labMotionIOC, 9, 0, 1, 1)
        self.currentSamp = QtWidgets.QLabel(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentSamp.sizePolicy().hasHeightForWidth())
        self.currentSamp.setSizePolicy(sizePolicy)
        self.currentSamp.setAutoFillBackground(False)
        self.currentSamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentSamp.setObjectName("currentSamp")
        self.robot_grid.addWidget(self.currentSamp, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButtonIOCCheck = QtWidgets.QPushButton(self.frameRobot)
        self.pushButtonIOCCheck.setObjectName("pushButtonIOCCheck")
        self.robot_grid.addWidget(self.pushButtonIOCCheck, 13, 0, 1, 1)
        self.gridLayout.addWidget(self.frameRobot, 3, 4, 1, 1)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 2, 2, 1, 1)
        self.oav_stream = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oav_stream.sizePolicy().hasHeightForWidth())
        self.oav_stream.setSizePolicy(sizePolicy)
        self.oav_stream.setMinimumSize(QtCore.QSize(0, 0))
        self.oav_stream.setMaximumSize(QtCore.QSize(2064, 1544))
        self.oav_stream.setSizeIncrement(QtCore.QSize(0, 0))
        self.oav_stream.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.oav_stream.setFrameShadow(QtWidgets.QFrame.Plain)
        self.oav_stream.setText("")
        self.oav_stream.setPixmap(QtGui.QPixmap("/Users/vwg85559/aithre/icon.png"))
        self.oav_stream.setScaledContents(True)
        self.oav_stream.setAlignment(QtCore.Qt.AlignCenter)
        self.oav_stream.setObjectName("oav_stream")
        self.gridLayout.addWidget(self.oav_stream, 0, 0, 2, 3)
        self.snapshot = QtWidgets.QPushButton(self.centralwidget)
        self.snapshot.setObjectName("snapshot")
        self.gridLayout.addWidget(self.snapshot, 2, 4, 1, 1)
        self.framePositionButtons = QtWidgets.QFrame(self.centralwidget)
        self.framePositionButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePositionButtons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.framePositionButtons.setObjectName("framePositionButtons")
        self.motion_grid = QtWidgets.QGridLayout(self.framePositionButtons)
        self.motion_grid.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.motion_grid.setSpacing(5)
        self.motion_grid.setObjectName("motion_grid")
        self.down = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.down.sizePolicy().hasHeightForWidth())
        self.down.setSizePolicy(sizePolicy)
        self.down.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("/Users/vwg85559/aithre/down.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.down.setIcon(icon1)
        self.down.setIconSize(QtCore.QSize(60, 60))
        self.down.setAutoRepeat(False)
        self.down.setAutoExclusive(False)
        self.down.setObjectName("down")
        self.motion_grid.addWidget(self.down, 2, 1, 1, 1)
        self.buttonFastOmegaTurn = QtWidgets.QPushButton(self.framePositionButtons)
        self.buttonFastOmegaTurn.setObjectName("buttonFastOmegaTurn")
        self.motion_grid.addWidget(self.buttonFastOmegaTurn, 2, 2, 1, 1)
        self.plus180 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus180.setObjectName("plus180")
        self.motion_grid.addWidget(self.plus180, 6, 3, 1, 1)
        self.left = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("/Users/vwg85559/aithre/left.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.left.setIcon(icon2)
        self.left.setIconSize(QtCore.QSize(60, 60))
        self.left.setObjectName("left")
        self.motion_grid.addWidget(self.left, 1, 0, 1, 1)
        self.minus90 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus90.setObjectName("minus90")
        self.motion_grid.addWidget(self.minus90, 5, 2, 1, 1)
        self.plus90 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus90.setObjectName("plus90")
        self.motion_grid.addWidget(self.plus90, 6, 2, 1, 1)
        self.plus15 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus15.setObjectName("plus15")
        self.motion_grid.addWidget(self.plus15, 6, 1, 1, 1)
        self.buttonSlowOmegaTurn = QtWidgets.QPushButton(self.framePositionButtons)
        self.buttonSlowOmegaTurn.setObjectName("buttonSlowOmegaTurn")
        self.motion_grid.addWidget(self.buttonSlowOmegaTurn, 2, 0, 1, 1)
        self.up = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy)
        self.up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("/Users/vwg85559/aithre/up.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.up.setIcon(icon3)
        self.up.setIconSize(QtCore.QSize(60, 60))
        self.up.setObjectName("up")
        self.motion_grid.addWidget(self.up, 0, 1, 1, 1)
        self.minus15 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus15.setObjectName("minus15")
        self.motion_grid.addWidget(self.minus15, 5, 1, 1, 1)
        self.minus5 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus5.setObjectName("minus5")
        self.motion_grid.addWidget(self.minus5, 5, 0, 1, 1)
        self.pushButtonSampleIn = QtWidgets.QPushButton(self.framePositionButtons)
        self.pushButtonSampleIn.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleIn.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleIn.setObjectName("pushButtonSampleIn")
        self.motion_grid.addWidget(self.pushButtonSampleIn, 0, 0, 1, 1)
        self.right = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("/Users/vwg85559/aithre/right.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On,
        )
        self.right.setIcon(icon4)
        self.right.setIconSize(QtCore.QSize(60, 60))
        self.right.setObjectName("right")
        self.motion_grid.addWidget(self.right, 1, 2, 1, 1)
        self.plus5 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus5.setObjectName("plus5")
        self.motion_grid.addWidget(self.plus5, 6, 0, 1, 1)
        self.minus180 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus180.setObjectName("minus180")
        self.motion_grid.addWidget(self.minus180, 5, 3, 1, 1)
        self.plusMinus3600 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plusMinus3600.setObjectName("plusMinus3600")
        self.motion_grid.addWidget(self.plusMinus3600, 0, 3, 1, 1)
        self.zero = QtWidgets.QPushButton(self.framePositionButtons)
        self.zero.setObjectName("zero")
        self.motion_grid.addWidget(self.zero, 2, 3, 1, 1)
        self.zeroAll = QtWidgets.QPushButton(self.framePositionButtons)
        self.zeroAll.setMinimumSize(QtCore.QSize(50, 50))
        self.zeroAll.setFlat(False)
        self.zeroAll.setObjectName("zeroAll")
        self.motion_grid.addWidget(self.zeroAll, 1, 1, 1, 1)
        self.pushButtonSampleOut = QtWidgets.QPushButton(self.framePositionButtons)
        self.pushButtonSampleOut.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButtonSampleOut.sizePolicy().hasHeightForWidth()
        )
        self.pushButtonSampleOut.setSizePolicy(sizePolicy)
        self.pushButtonSampleOut.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleOut.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButtonSampleOut.setAutoDefault(False)
        self.pushButtonSampleOut.setDefault(False)
        self.pushButtonSampleOut.setFlat(False)
        self.pushButtonSampleOut.setObjectName("pushButtonSampleOut")
        self.motion_grid.addWidget(self.pushButtonSampleOut, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.framePositionButtons, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 957, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuIOCs = QtWidgets.QMenu(self.menuBar)
        self.menuIOCs.setObjectName("menuIOCs")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_log = QtWidgets.QAction(MainWindow)
        self.actionSave_log.setObjectName("actionSave_log")
        self.actionRestart_OAV_IOC = QtWidgets.QAction(MainWindow)
        self.actionRestart_OAV_IOC.setObjectName("actionRestart_OAV_IOC")
        self.actionRestart_Robot_IOC = QtWidgets.QAction(MainWindow)
        self.actionRestart_Robot_IOC.setObjectName("actionRestart_Robot_IOC")
        self.actionRestart_Gonio_IOC = QtWidgets.QAction(MainWindow)
        self.actionRestart_Gonio_IOC.setObjectName("actionRestart_Gonio_IOC")
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionSave_log)
        self.menuIOCs.addAction(self.actionRestart_OAV_IOC)
        self.menuIOCs.addAction(self.actionRestart_Robot_IOC)
        self.menuIOCs.addAction(self.actionRestart_Gonio_IOC)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuIOCs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.load, self.unload)
        MainWindow.setTabOrder(self.unload, self.spinToLoad)
        MainWindow.setTabOrder(self.spinToLoad, self.dry)
        MainWindow.setTabOrder(self.dry, self.start)
        MainWindow.setTabOrder(self.start, self.stop)
        MainWindow.setTabOrder(self.stop, self.sliderExposure)
        MainWindow.setTabOrder(self.sliderExposure, self.sliderGain)
        MainWindow.setTabOrder(self.sliderGain, self.stagez_request)
        MainWindow.setTabOrder(self.stagez_request, self.gony_request)
        MainWindow.setTabOrder(self.gony_request, self.gonz_request)
        MainWindow.setTabOrder(self.gonz_request, self.omega_request)
        MainWindow.setTabOrder(self.omega_request, self.up)
        MainWindow.setTabOrder(self.up, self.down)
        MainWindow.setTabOrder(self.down, self.left)
        MainWindow.setTabOrder(self.left, self.right)
        MainWindow.setTabOrder(self.right, self.minus5)
        MainWindow.setTabOrder(self.minus5, self.snapshot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Aithre v4.2 - I23 Laser Shaping")
        )
        self.gony_rbv.setText(_translate("MainWindow", "0.12"))
        self.gain_rbv.setText(_translate("MainWindow", "0"))
        self.exposure_rbv.setText(_translate("MainWindow", "0.04"))
        self.openOAVZoom.setText(_translate("MainWindow", "Open OAV Zoom Window"))
        self.labY.setText(_translate("MainWindow", "Y"))
        self.omega_rbv.setText(_translate("MainWindow", "0.00"))
        self.labOmega.setText(_translate("MainWindow", "Omega"))
        self.labGain.setText(_translate("MainWindow", "Gain"))
        self.labstageZ.setText(_translate("MainWindow", "Stage Z"))
        self.gonz_rbv.setText(_translate("MainWindow", "0.55"))
        self.labExposure.setText(_translate("MainWindow", "Exposure"))
        self.stagez_rbv.setText(_translate("MainWindow", "0.352"))
        self.labZ.setText(_translate("MainWindow", "Z"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.unload.setText(_translate("MainWindow", "Unload"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.labBeamlineSafe.setText(_translate("MainWindow", "Beamline Safe"))
        self.labRobotIOC.setText(_translate("MainWindow", "Robot IOC"))
        self.labZoomIOC.setText(_translate("MainWindow", "Zoom IOC"))
        self.labOAVIOC.setText(_translate("MainWindow", "OAV IOC"))
        self.resetRobot.setText(_translate("MainWindow", "Reset"))
        self.labRobotActive.setText(_translate("MainWindow", "Robot Active"))
        self.labGonioSensor.setText(_translate("MainWindow", "Gonio Sensor"))
        self.goHomeRobot.setText(_translate("MainWindow", "Go Home"))
        self.dry.setText(_translate("MainWindow", "Dry"))
        self.labCurrentSamp.setText(_translate("MainWindow", "Current Sample"))
        self.labMotionIOC.setText(_translate("MainWindow", "Motion IOC"))
        self.currentSamp.setText(_translate("MainWindow", "0"))
        self.pushButtonIOCCheck.setText(_translate("MainWindow", "IOC Check"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.buttonFastOmegaTurn.setText(_translate("MainWindow", "Fast Turn"))
        self.plus180.setText(_translate("MainWindow", "+180"))
        self.minus90.setText(_translate("MainWindow", "-90"))
        self.plus90.setText(_translate("MainWindow", "+90"))
        self.plus15.setText(_translate("MainWindow", "+15"))
        self.buttonSlowOmegaTurn.setText(_translate("MainWindow", "Slow Turn"))
        self.minus15.setText(_translate("MainWindow", "-15"))
        self.minus5.setText(_translate("MainWindow", "-5"))
        self.pushButtonSampleIn.setText(_translate("MainWindow", "In"))
        self.plus5.setText(_translate("MainWindow", "+5"))
        self.minus180.setText(_translate("MainWindow", "-180"))
        self.plusMinus3600.setText(_translate("MainWindow", "+/- 3600"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.zeroAll.setText(_translate("MainWindow", "ZeroAll"))
        self.pushButtonSampleOut.setText(_translate("MainWindow", "Out"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuIOCs.setTitle(_translate("MainWindow", "IOCs"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_log.setText(_translate("MainWindow", "Save log"))
        self.actionRestart_OAV_IOC.setText(_translate("MainWindow", "Restart OAV IOC"))
        self.actionRestart_Robot_IOC.setText(
            _translate("MainWindow", "Restart Robot IOC")
        )
        self.actionRestart_Gonio_IOC.setText(
            _translate("MainWindow", "Restart Gonio IOC")
        )
