# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiv4.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 874)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label = QtWidgets.QLabel(self.frameFineControl)
        self.label.setObjectName("label")
        self.readback_grid.addWidget(self.label, 1, 1, 1, 1)
        self.labZ = QtWidgets.QLabel(self.frameFineControl)
        self.labZ.setAlignment(QtCore.Qt.AlignCenter)
        self.labZ.setObjectName("labZ")
        self.readback_grid.addWidget(self.labZ, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frameFineControl)
        self.label_2.setObjectName("label_2")
        self.readback_grid.addWidget(self.label_2, 2, 1, 1, 1)
        self.gony_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.gony_rbv.setObjectName("gony_rbv")
        self.readback_grid.addWidget(self.gony_rbv, 4, 1, 1, 1)
        self.gony_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.gony_request.setMaxLength(5)
        self.gony_request.setObjectName("gony_request")
        self.readback_grid.addWidget(self.gony_request, 4, 3, 1, 1)
        self.labZoom = QtWidgets.QLabel(self.frameFineControl)
        self.labZoom.setObjectName("labZoom")
        self.readback_grid.addWidget(self.labZoom, 0, 0, 1, 1)
        self.labGain = QtWidgets.QLabel(self.frameFineControl)
        self.labGain.setObjectName("labGain")
        self.readback_grid.addWidget(self.labGain, 2, 0, 1, 1)
        self.gonz_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.gonz_request.setMaxLength(5)
        self.gonz_request.setObjectName("gonz_request")
        self.readback_grid.addWidget(self.gonz_request, 5, 3, 1, 1)
        self.stagex_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.stagex_rbv.setObjectName("stagex_rbv")
        self.readback_grid.addWidget(self.stagex_rbv, 3, 1, 1, 1)
        self.labExposure = QtWidgets.QLabel(self.frameFineControl)
        self.labExposure.setObjectName("labExposure")
        self.readback_grid.addWidget(self.labExposure, 1, 0, 1, 1)
        self.sliderGain = QtWidgets.QSlider(self.frameFineControl)
        self.sliderGain.setMaximum(100)
        self.sliderGain.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGain.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.sliderGain.setTickInterval(5)
        self.sliderGain.setObjectName("sliderGain")
        self.readback_grid.addWidget(self.sliderGain, 2, 3, 1, 1)
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
        self.zoomSelect = QtWidgets.QComboBox(self.frameFineControl)
        self.zoomSelect.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.zoomSelect.setObjectName("zoomSelect")
        self.zoomSelect.addItem("")
        self.zoomSelect.addItem("")
        self.zoomSelect.addItem("")
        self.zoomSelect.addItem("")
        self.readback_grid.addWidget(self.zoomSelect, 0, 3, 1, 1)
        self.omega_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.omega_request.setMaxLength(5)
        self.omega_request.setObjectName("omega_request")
        self.readback_grid.addWidget(self.omega_request, 7, 3, 1, 1)
        self.stagex_request = QtWidgets.QLineEdit(self.frameFineControl)
        self.stagex_request.setText("")
        self.stagex_request.setMaxLength(5)
        self.stagex_request.setObjectName("stagex_request")
        self.readback_grid.addWidget(self.stagex_request, 3, 3, 1, 1)
        self.gonz_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.gonz_rbv.setObjectName("gonz_rbv")
        self.readback_grid.addWidget(self.gonz_rbv, 5, 1, 1, 1)
        self.omega_rbv = QtWidgets.QLabel(self.frameFineControl)
        self.omega_rbv.setObjectName("omega_rbv")
        self.readback_grid.addWidget(self.omega_rbv, 7, 1, 1, 1)
        self.labOmega = QtWidgets.QLabel(self.frameFineControl)
        self.labOmega.setAlignment(QtCore.Qt.AlignCenter)
        self.labOmega.setObjectName("labOmega")
        self.readback_grid.addWidget(self.labOmega, 7, 0, 1, 1)
        self.labX = QtWidgets.QLabel(self.frameFineControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labX.sizePolicy().hasHeightForWidth())
        self.labX.setSizePolicy(sizePolicy)
        self.labX.setAlignment(QtCore.Qt.AlignCenter)
        self.labX.setObjectName("labX")
        self.readback_grid.addWidget(self.labX, 3, 0, 1, 1)
        self.labY = QtWidgets.QLabel(self.frameFineControl)
        self.labY.setAlignment(QtCore.Qt.AlignCenter)
        self.labY.setObjectName("labY")
        self.readback_grid.addWidget(self.labY, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frameFineControl, 2, 2, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 1, 0, 1, 1)
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 1, 2, 1, 1)
        self.snapshot = QtWidgets.QPushButton(self.centralwidget)
        self.snapshot.setObjectName("snapshot")
        self.gridLayout.addWidget(self.snapshot, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.oav_stream = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oav_stream.sizePolicy().hasHeightForWidth())
        self.oav_stream.setSizePolicy(sizePolicy)
        self.oav_stream.setText("")
        self.oav_stream.setPixmap(QtGui.QPixmap("icon.png"))
        self.oav_stream.setScaledContents(True)
        self.oav_stream.setAlignment(QtCore.Qt.AlignCenter)
        self.oav_stream.setObjectName("oav_stream")
        self.gridLayout.addWidget(self.oav_stream, 0, 0, 1, 5)
        self.framePositionButtons = QtWidgets.QFrame(self.centralwidget)
        self.framePositionButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePositionButtons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.framePositionButtons.setObjectName("framePositionButtons")
        self.motion_grid = QtWidgets.QGridLayout(self.framePositionButtons)
        self.motion_grid.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.motion_grid.setSpacing(5)
        self.motion_grid.setObjectName("motion_grid")
        self.up = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up.sizePolicy().hasHeightForWidth())
        self.up.setSizePolicy(sizePolicy)
        self.up.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.up.setIcon(icon1)
        self.up.setIconSize(QtCore.QSize(60, 60))
        self.up.setObjectName("up")
        self.motion_grid.addWidget(self.up, 0, 1, 1, 1)
        self.minus90 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus90.setObjectName("minus90")
        self.motion_grid.addWidget(self.minus90, 3, 2, 1, 1)
        self.plus5 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus5.setObjectName("plus5")
        self.motion_grid.addWidget(self.plus5, 4, 0, 1, 1)
        self.plus90 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus90.setObjectName("plus90")
        self.motion_grid.addWidget(self.plus90, 4, 2, 1, 1)
        self.plu15 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plu15.setObjectName("plu15")
        self.motion_grid.addWidget(self.plu15, 4, 1, 1, 1)
        self.down = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.down.sizePolicy().hasHeightForWidth())
        self.down.setSizePolicy(sizePolicy)
        self.down.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.down.setIcon(icon2)
        self.down.setIconSize(QtCore.QSize(60, 60))
        self.down.setAutoRepeat(False)
        self.down.setAutoExclusive(False)
        self.down.setObjectName("down")
        self.motion_grid.addWidget(self.down, 2, 1, 1, 1)
        self.minus180 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus180.setObjectName("minus180")
        self.motion_grid.addWidget(self.minus180, 3, 3, 1, 1)
        self.minus5 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus5.setObjectName("minus5")
        self.motion_grid.addWidget(self.minus5, 3, 0, 1, 1)
        self.minus15 = QtWidgets.QPushButton(self.framePositionButtons)
        self.minus15.setObjectName("minus15")
        self.motion_grid.addWidget(self.minus15, 3, 1, 1, 1)
        self.plus180 = QtWidgets.QPushButton(self.framePositionButtons)
        self.plus180.setObjectName("plus180")
        self.motion_grid.addWidget(self.plus180, 4, 3, 1, 1)
        self.left = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left.setIcon(icon3)
        self.left.setIconSize(QtCore.QSize(60, 60))
        self.left.setObjectName("left")
        self.motion_grid.addWidget(self.left, 1, 0, 1, 1)
        self.right = QtWidgets.QPushButton(self.framePositionButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.right.setIcon(icon4)
        self.right.setIconSize(QtCore.QSize(60, 60))
        self.right.setObjectName("right")
        self.motion_grid.addWidget(self.right, 1, 2, 1, 1)
        self.zero = QtWidgets.QPushButton(self.framePositionButtons)
        self.zero.setObjectName("zero")
        self.motion_grid.addWidget(self.zero, 2, 3, 1, 1)
        self.zeroAll = QtWidgets.QPushButton(self.framePositionButtons)
        self.zeroAll.setFlat(False)
        self.zeroAll.setObjectName("zeroAll")
        self.motion_grid.addWidget(self.zeroAll, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.framePositionButtons, 2, 0, 1, 1)
        self.frameRobot = QtWidgets.QFrame(self.centralwidget)
        self.frameRobot.setAutoFillBackground(False)
        self.frameRobot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRobot.setObjectName("frameRobot")
        self.robot_grid = QtWidgets.QGridLayout(self.frameRobot)
        self.robot_grid.setObjectName("robot_grid")
        self.spinBox = QtWidgets.QSpinBox(self.frameRobot)
        self.spinBox.setProperty("showGroupSeparator", False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(16)
        self.spinBox.setObjectName("spinBox")
        self.robot_grid.addWidget(self.spinBox, 3, 1, 1, 1)
        self.gonioSens = QtWidgets.QLabel(self.frameRobot)
        self.gonioSens.setMinimumSize(QtCore.QSize(20, 20))
        self.gonioSens.setMaximumSize(QtCore.QSize(20, 20))
        self.gonioSens.setText("")
        self.gonioSens.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gonioSens.setObjectName("gonioSens")
        self.robot_grid.addWidget(self.gonioSens, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.labGonioSens = QtWidgets.QLabel(self.frameRobot)
        self.labGonioSens.setObjectName("labGonioSens")
        self.robot_grid.addWidget(self.labGonioSens, 1, 0, 1, 1)
        self.load = QtWidgets.QPushButton(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load.sizePolicy().hasHeightForWidth())
        self.load.setSizePolicy(sizePolicy)
        self.load.setObjectName("load")
        self.robot_grid.addWidget(self.load, 3, 0, 1, 1)
        self.currentsamp = QtWidgets.QLabel(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentsamp.sizePolicy().hasHeightForWidth())
        self.currentsamp.setSizePolicy(sizePolicy)
        self.currentsamp.setAutoFillBackground(False)
        self.currentsamp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentsamp.setObjectName("currentsamp")
        self.robot_grid.addWidget(self.currentsamp, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.labCurrentSamp = QtWidgets.QLabel(self.frameRobot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labCurrentSamp.sizePolicy().hasHeightForWidth())
        self.labCurrentSamp.setSizePolicy(sizePolicy)
        self.labCurrentSamp.setObjectName("labCurrentSamp")
        self.robot_grid.addWidget(self.labCurrentSamp, 0, 0, 1, 1)
        self.unload = QtWidgets.QPushButton(self.frameRobot)
        self.unload.setObjectName("unload")
        self.robot_grid.addWidget(self.unload, 4, 0, 1, 1)
        self.dry = QtWidgets.QPushButton(self.frameRobot)
        self.dry.setObjectName("dry")
        self.robot_grid.addWidget(self.dry, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.robot_grid.addItem(spacerItem2, 2, 0, 1, 2)
        self.gridLayout.addWidget(self.frameRobot, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1088, 24))
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
        self.zoomSelect.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.load, self.unload)
        MainWindow.setTabOrder(self.unload, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.dry)
        MainWindow.setTabOrder(self.dry, self.start)
        MainWindow.setTabOrder(self.start, self.stop)
        MainWindow.setTabOrder(self.stop, self.sliderExposure)
        MainWindow.setTabOrder(self.sliderExposure, self.sliderGain)
        MainWindow.setTabOrder(self.sliderGain, self.stagex_request)
        MainWindow.setTabOrder(self.stagex_request, self.gony_request)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Aithre v4.1 - I23 Laser Shaping"))
        self.label.setText(_translate("MainWindow", "0.04"))
        self.labZ.setText(_translate("MainWindow", "Z"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.gony_rbv.setText(_translate("MainWindow", "0.12"))
        self.labZoom.setText(_translate("MainWindow", "Zoom"))
        self.labGain.setText(_translate("MainWindow", "Gain"))
        self.stagex_rbv.setText(_translate("MainWindow", "0.352"))
        self.labExposure.setText(_translate("MainWindow", "Exposure"))
        self.zoomSelect.setCurrentText(_translate("MainWindow", "1"))
        self.zoomSelect.setItemText(0, _translate("MainWindow", "1"))
        self.zoomSelect.setItemText(1, _translate("MainWindow", "2"))
        self.zoomSelect.setItemText(2, _translate("MainWindow", "4"))
        self.zoomSelect.setItemText(3, _translate("MainWindow", "8"))
        self.gonz_rbv.setText(_translate("MainWindow", "0.55"))
        self.omega_rbv.setText(_translate("MainWindow", "0.00"))
        self.labOmega.setText(_translate("MainWindow", "Omega"))
        self.labX.setText(_translate("MainWindow", "X"))
        self.labY.setText(_translate("MainWindow", "Y"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.snapshot.setText(_translate("MainWindow", "Snapshot"))
        self.minus90.setText(_translate("MainWindow", "-90"))
        self.plus5.setText(_translate("MainWindow", "+5"))
        self.plus90.setText(_translate("MainWindow", "+90"))
        self.plu15.setText(_translate("MainWindow", "+15"))
        self.minus180.setText(_translate("MainWindow", "-180"))
        self.minus5.setText(_translate("MainWindow", "-5"))
        self.minus15.setText(_translate("MainWindow", "-15"))
        self.plus180.setText(_translate("MainWindow", "+180"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.zeroAll.setText(_translate("MainWindow", "ZeroAll"))
        self.labGonioSens.setText(_translate("MainWindow", "Gonio Sensor"))
        self.load.setText(_translate("MainWindow", "Load"))
        self.currentsamp.setText(_translate("MainWindow", "0"))
        self.labCurrentSamp.setText(_translate("MainWindow", "Current Sample"))
        self.unload.setText(_translate("MainWindow", "Unload"))
        self.dry.setText(_translate("MainWindow", "Dry"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuIOCs.setTitle(_translate("MainWindow", "IOCs"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_log.setText(_translate("MainWindow", "Save log"))
        self.actionRestart_OAV_IOC.setText(_translate("MainWindow", "Restart OAV IOC"))
        self.actionRestart_Robot_IOC.setText(_translate("MainWindow", "Restart Robot IOC"))
        self.actionRestart_Gonio_IOC.setText(_translate("MainWindow", "Restart Gonio IOC"))