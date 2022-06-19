# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_ui/main_fa.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 635)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 635))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(711, 526))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInstructors = QtWidgets.QWidget()
        self.tabInstructors.setObjectName("tabInstructors")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabInstructors)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tabInstructors)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnInstrAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnInstrAdd.setObjectName("btnInstrAdd")
        self.horizontalLayout.addWidget(self.btnInstrAdd)
        self.btnInstrImport = QtWidgets.QPushButton(self.groupBox)
        self.btnInstrImport.setObjectName("btnInstrImport")
        self.horizontalLayout.addWidget(self.btnInstrImport)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tabInstructors)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txtEditInsSearch = QtWidgets.QLineEdit(self.groupBox_11)
        self.txtEditInsSearch.setObjectName("txtEditInsSearch")
        self.horizontalLayout_6.addWidget(self.txtEditInsSearch)
        self.verticalLayout_2.addWidget(self.groupBox_11)
        self.treeInstr = QtWidgets.QTreeView(self.tabInstructors)
        self.treeInstr.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeInstr.sizePolicy().hasHeightForWidth())
        self.treeInstr.setSizePolicy(sizePolicy)
        self.treeInstr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeInstr.setObjectName("treeInstr")
        self.verticalLayout_2.addWidget(self.treeInstr)
        self.tabWidget.addTab(self.tabInstructors, "")
        self.tabRooms = QtWidgets.QWidget()
        self.tabRooms.setObjectName("tabRooms")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabRooms)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabRooms)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnRoomAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRoomAdd.setObjectName("btnRoomAdd")
        self.horizontalLayout_7.addWidget(self.btnRoomAdd)
        self.btnRoomImport = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRoomImport.setObjectName("btnRoomImport")
        self.horizontalLayout_7.addWidget(self.btnRoomImport)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tabRooms)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.txtSearchRoom = QtWidgets.QLineEdit(self.groupBox_10)
        self.txtSearchRoom.setObjectName("txtSearchRoom")
        self.horizontalLayout_8.addWidget(self.txtSearchRoom)
        self.verticalLayout_3.addWidget(self.groupBox_10)
        self.treeRoom = QtWidgets.QTreeView(self.tabRooms)
        self.treeRoom.setObjectName("treeRoom")
        self.verticalLayout_3.addWidget(self.treeRoom)
        self.tabWidget.addTab(self.tabRooms, "")
        self.tabSubjects = QtWidgets.QWidget()
        self.tabSubjects.setObjectName("tabSubjects")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSubjects)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabSubjects)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSubjAdd = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSubjAdd.setObjectName("btnSubjAdd")
        self.horizontalLayout_2.addWidget(self.btnSubjAdd)
        self.btnSubjImport = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSubjImport.setObjectName("btnSubjImport")
        self.horizontalLayout_2.addWidget(self.btnSubjImport)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tabSubjects)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.txtSearchSubject = QtWidgets.QLineEdit(self.groupBox_12)
        self.txtSearchSubject.setObjectName("txtSearchSubject")
        self.horizontalLayout_9.addWidget(self.txtSearchSubject)
        self.verticalLayout_4.addWidget(self.groupBox_12)
        self.treeSubj = QtWidgets.QTreeView(self.tabSubjects)
        self.treeSubj.setObjectName("treeSubj")
        self.verticalLayout_4.addWidget(self.treeSubj)
        self.tabWidget.addTab(self.tabSubjects, "")
        self.tabSections = QtWidgets.QWidget()
        self.tabSections.setObjectName("tabSections")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabSections)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tabSections)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSecAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnSecAdd.setObjectName("btnSecAdd")
        self.horizontalLayout_3.addWidget(self.btnSecAdd)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.treeSec = QtWidgets.QTreeView(self.tabSections)
        self.treeSec.setObjectName("treeSec")
        self.verticalLayout_5.addWidget(self.treeSec)
        self.tabWidget.addTab(self.tabSections, "")
        self.tabScenario = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabScenario.sizePolicy().hasHeightForWidth())
        self.tabScenario.setSizePolicy(sizePolicy)
        self.tabScenario.setObjectName("tabScenario")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabScenario)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnScenGenerate = QtWidgets.QPushButton(self.groupBox_5)
        self.btnScenGenerate.setObjectName("btnScenGenerate")
        self.horizontalLayout_4.addWidget(self.btnScenGenerate)
        self.btnScenResult = QtWidgets.QPushButton(self.groupBox_5)
        self.btnScenResult.setObjectName("btnScenResult")
        self.horizontalLayout_4.addWidget(self.btnScenResult)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setStyleSheet("border: none")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioLunchYes = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioLunchYes.setChecked(True)
        self.radioLunchYes.setObjectName("radioLunchYes")
        self.horizontalLayout_5.addWidget(self.radioLunchYes)
        self.radioLunchNo = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioLunchNo.setObjectName("radioLunchNo")
        self.horizontalLayout_5.addWidget(self.radioLunchNo)
        self.gridLayout_2.addWidget(self.groupBox_7, 0, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.editMinPop = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMinPop.setMinimum(10)
        self.editMinPop.setMaximum(10000)
        self.editMinPop.setObjectName("editMinPop")
        self.gridLayout_3.addWidget(self.editMinPop, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 3, 1, 1)
        self.editMut = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.editMut.setMaximum(100.0)
        self.editMut.setSingleStep(0.01)
        self.editMut.setProperty("value", 0.08)
        self.editMut.setObjectName("editMut")
        self.gridLayout_3.addWidget(self.editMut, 0, 5, 1, 1)
        self.editMaxFit = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxFit.setMaximum(100)
        self.editMaxFit.setProperty("value", 90)
        self.editMaxFit.setObjectName("editMaxFit")
        self.gridLayout_3.addWidget(self.editMaxFit, 1, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 7, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_8)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 4, 3, 1, 1)
        self.editMaxGen = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxGen.setMinimum(50)
        self.editMaxGen.setMaximum(10000)
        self.editMaxGen.setObjectName("editMaxGen")
        self.gridLayout_3.addWidget(self.editMaxGen, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_8)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_8)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.editElite = QtWidgets.QSpinBox(self.groupBox_8)
        self.editElite.setMaximum(100)
        self.editElite.setProperty("value", 5)
        self.editElite.setObjectName("editElite")
        self.gridLayout_3.addWidget(self.editElite, 2, 5, 1, 1)
        self.editMutStep = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.editMutStep.setProperty("value", 0.05)
        self.editMutStep.setObjectName("editMutStep")
        self.gridLayout_3.addWidget(self.editMutStep, 4, 5, 1, 1)
        self.editMaxPop = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxPop.setMinimum(10)
        self.editMaxPop.setMaximum(10000)
        self.editMaxPop.setProperty("value", 100)
        self.editMaxPop.setObjectName("editMaxPop")
        self.gridLayout_3.addWidget(self.editMaxPop, 1, 1, 1, 1)
        self.editDev = QtWidgets.QSpinBox(self.groupBox_8)
        self.editDev.setMaximum(100)
        self.editDev.setProperty("value", 55)
        self.editDev.setObjectName("editDev")
        self.gridLayout_3.addWidget(self.editDev, 3, 5, 1, 1)
        self.editBaseMut = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.editBaseMut.setProperty("value", 0.1)
        self.editBaseMut.setObjectName("editBaseMut")
        self.gridLayout_3.addWidget(self.editBaseMut, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_8)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.editMaxCreation = QtWidgets.QSpinBox(self.groupBox_8)
        self.editMaxCreation.setMinimum(1500)
        self.editMaxCreation.setMaximum(30000)
        self.editMaxCreation.setObjectName("editMaxCreation")
        self.gridLayout_3.addWidget(self.editMaxCreation, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_8)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 3, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tabScenario)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.editIdle = QtWidgets.QSpinBox(self.groupBox_9)
        self.editIdle.setMaximum(100)
        self.editIdle.setProperty("value", 5)
        self.editIdle.setObjectName("editIdle")
        self.gridLayout_4.addWidget(self.editIdle, 1, 1, 1, 1)
        self.editSbj = QtWidgets.QSpinBox(self.groupBox_9)
        self.editSbj.setMaximum(100)
        self.editSbj.setProperty("value", 70)
        self.editSbj.setObjectName("editSbj")
        self.gridLayout_4.addWidget(self.editSbj, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_9)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)
        self.lblTotal = QtWidgets.QLabel(self.groupBox_9)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout_4.addWidget(self.lblTotal, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.tabWidget.addTab(self.tabScenario, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Instructor = QtWidgets.QAction(MainWindow)
        self.actionAdd_Instructor.setObjectName("actionAdd_Instructor")
        self.actionView_Instructors = QtWidgets.QAction(MainWindow)
        self.actionView_Instructors.setObjectName("actionView_Instructors")
        self.actionAdd_Room = QtWidgets.QAction(MainWindow)
        self.actionAdd_Room.setObjectName("actionAdd_Room")
        self.actionView_Rooms = QtWidgets.QAction(MainWindow)
        self.actionView_Rooms.setObjectName("actionView_Rooms")
        self.actionAdd_Subject = QtWidgets.QAction(MainWindow)
        self.actionAdd_Subject.setObjectName("actionAdd_Subject")
        self.actionView_Subjects = QtWidgets.QAction(MainWindow)
        self.actionView_Subjects.setObjectName("actionView_Subjects")
        self.actionAdd_Sections = QtWidgets.QAction(MainWindow)
        self.actionAdd_Sections.setObjectName("actionAdd_Sections")
        self.actionView_Sections = QtWidgets.QAction(MainWindow)
        self.actionView_Sections.setObjectName("actionView_Sections")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionView_Results = QtWidgets.QAction(MainWindow)
        self.actionView_Results.setObjectName("actionView_Results")
        self.actionGenerate = QtWidgets.QAction(MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionImport_2 = QtWidgets.QAction(MainWindow)
        self.actionImport_2.setObjectName("actionImport_2")
        self.actionExport_2 = QtWidgets.QAction(MainWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionScenario_Summary = QtWidgets.QAction(MainWindow)
        self.actionScenario_Summary.setObjectName("actionScenario_Summary")
        self.actionGenerate_2 = QtWidgets.QAction(MainWindow)
        self.actionGenerate_2.setObjectName("actionGenerate_2")
        self.actionView_Results_2 = QtWidgets.QAction(MainWindow)
        self.actionView_Results_2.setObjectName("actionView_Results_2")
        self.actionInstructions = QtWidgets.QAction(MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.btnInstrAdd)
        MainWindow.setTabOrder(self.btnInstrAdd, self.btnInstrImport)
        MainWindow.setTabOrder(self.btnInstrImport, self.txtEditInsSearch)
        MainWindow.setTabOrder(self.txtEditInsSearch, self.treeInstr)
        MainWindow.setTabOrder(self.treeInstr, self.btnRoomAdd)
        MainWindow.setTabOrder(self.btnRoomAdd, self.btnRoomImport)
        MainWindow.setTabOrder(self.btnRoomImport, self.treeRoom)
        MainWindow.setTabOrder(self.treeRoom, self.btnSubjAdd)
        MainWindow.setTabOrder(self.btnSubjAdd, self.btnSubjImport)
        MainWindow.setTabOrder(self.btnSubjImport, self.treeSubj)
        MainWindow.setTabOrder(self.treeSubj, self.btnSecAdd)
        MainWindow.setTabOrder(self.btnSecAdd, self.treeSec)
        MainWindow.setTabOrder(self.treeSec, self.radioLunchYes)
        MainWindow.setTabOrder(self.radioLunchYes, self.radioLunchNo)
        MainWindow.setTabOrder(self.radioLunchNo, self.editMinPop)
        MainWindow.setTabOrder(self.editMinPop, self.editMaxPop)
        MainWindow.setTabOrder(self.editMaxPop, self.editMaxGen)
        MainWindow.setTabOrder(self.editMaxGen, self.editMaxCreation)
        MainWindow.setTabOrder(self.editMaxCreation, self.editMut)
        MainWindow.setTabOrder(self.editMut, self.editMaxFit)
        MainWindow.setTabOrder(self.editMaxFit, self.editElite)
        MainWindow.setTabOrder(self.editElite, self.editDev)
        MainWindow.setTabOrder(self.editDev, self.editSbj)
        MainWindow.setTabOrder(self.editSbj, self.editIdle)
        MainWindow.setTabOrder(self.editIdle, self.btnScenGenerate)
        MainWindow.setTabOrder(self.btnScenGenerate, self.btnScenResult)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genetic Algorithm Scheduler"))
        self.tabInstructors.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "عملیات"))
        self.btnInstrAdd.setText(_translate("MainWindow", "اضافه کردن استاد جدید"))
        self.btnInstrImport.setText(_translate("MainWindow", "بارگذاری از فایل اکسل"))
        self.groupBox_11.setTitle(_translate("MainWindow", "جست و جو"))
        self.txtEditInsSearch.setPlaceholderText(_translate("MainWindow", "جست و حو ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInstructors), _translate("MainWindow", "اساتید"))
        self.groupBox_2.setTitle(_translate("MainWindow", "عملیات"))
        self.btnRoomAdd.setText(_translate("MainWindow", "اضافه کردن کلاس جدید"))
        self.btnRoomImport.setText(_translate("MainWindow", "بارگذاری از فایل اکسل"))
        self.groupBox_10.setTitle(_translate("MainWindow", "جست و جو"))
        self.txtSearchRoom.setPlaceholderText(_translate("MainWindow", "جست و جو ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRooms), _translate("MainWindow", "کلاس ها"))
        self.groupBox_3.setTitle(_translate("MainWindow", "عملیات"))
        self.btnSubjAdd.setText(_translate("MainWindow", "اضافه کردن واحد جدید"))
        self.btnSubjImport.setText(_translate("MainWindow", "بارگذاری از فایل اکسل"))
        self.groupBox_12.setTitle(_translate("MainWindow", "جست و جو"))
        self.txtSearchSubject.setPlaceholderText(_translate("MainWindow", "جست و جو ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSubjects), _translate("MainWindow", "واحد ها"))
        self.groupBox_4.setTitle(_translate("MainWindow", "عملیات"))
        self.btnSecAdd.setText(_translate("MainWindow", "اضافه کردن گروه درسی جدید"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSections), _translate("MainWindow", "گروه ها"))
        self.groupBox_5.setTitle(_translate("MainWindow", "عملیات"))
        self.btnScenGenerate.setText(_translate("MainWindow", "ایجاد برنامه ریزی جدید"))
        self.btnScenResult.setText(_translate("MainWindow", "دریافت خروجی اکسل"))
        self.groupBox_6.setTitle(_translate("MainWindow", "تنظیمات عملیات"))
        self.label_6.setToolTip(_translate("MainWindow", "Assess for lunch break for sections."))
        self.label_6.setText(_translate("MainWindow", "تایم ناهار و نماز"))
        self.radioLunchYes.setText(_translate("MainWindow", "بله"))
        self.radioLunchNo.setText(_translate("MainWindow", "خیر"))
        self.groupBox_8.setTitle(_translate("MainWindow", "تنظیمات الگوریتم ژنتیک"))
        self.label_10.setToolTip(_translate("MainWindow", "Maximum attempts for creating a valid chromosome."))
        self.label_10.setText(_translate("MainWindow", "حداکثر کروموزم جدید"))
        self.label_12.setToolTip(_translate("MainWindow", "Stops the generation when a chromosome meets this."))
        self.label_12.setText(_translate("MainWindow", "حداکثر فیتنس"))
        self.label_11.setToolTip(_translate("MainWindow", "<html><head/><body><p>Triggers mutation rate change when the difference of average fitness falls to the specificied level.</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "فعال کننده نرخ جهش"))
        self.label_2.setText(_translate("MainWindow", "Mutation Rate Step"))
        self.label_21.setToolTip(_translate("MainWindow", "The maximum control of a sigma."))
        self.label_21.setText(_translate("MainWindow", "Deviation Tolerance"))
        self.label.setText(_translate("MainWindow", "نرخ پایه جهش"))
        self.label_9.setToolTip(_translate("MainWindow", "Maximum amount of generations to be performed on solution generation."))
        self.label_9.setText(_translate("MainWindow", "حداکثر تعداد نسل ها"))
        self.label_7.setToolTip(_translate("MainWindow", "Starting point and lowest population count of the genetic algorithm."))
        self.label_7.setText(_translate("MainWindow", "حداقل تعداد جمعیت"))
        self.label_8.setToolTip(_translate("MainWindow", "Highest population count of the genetic algorithm."))
        self.label_8.setText(_translate("MainWindow", "حداکثر تعداد جمعیت"))
        self.label_20.setToolTip(_translate("MainWindow", "The percent of population that would belong to elite."))
        self.label_20.setText(_translate("MainWindow", "تعداد جمعیت elite"))
        self.groupBox_9.setTitle(_translate("MainWindow", "ماتریس ارزیابی"))
        self.label_13.setToolTip(_translate("MainWindow", "The weight of having all subjects placed."))
        self.label_13.setText(_translate("MainWindow", "Subject Placement"))
        self.label_18.setToolTip(_translate("MainWindow", "The weight of sections having less idle time."))
        self.label_18.setText(_translate("MainWindow", "Instructor Idle Time"))
        self.lblTotal.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScenario), _translate("MainWindow", "مدیریت سناریو"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd_Instructor.setText(_translate("MainWindow", "Add Instructor"))
        self.actionView_Instructors.setText(_translate("MainWindow", "View Instructors"))
        self.actionAdd_Room.setText(_translate("MainWindow", "Add Room"))
        self.actionView_Rooms.setText(_translate("MainWindow", "View Rooms"))
        self.actionAdd_Subject.setText(_translate("MainWindow", "Add Subject"))
        self.actionView_Subjects.setText(_translate("MainWindow", "View Subjects"))
        self.actionAdd_Sections.setText(_translate("MainWindow", "Add Sections"))
        self.actionView_Sections.setText(_translate("MainWindow", "View Sections"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionView_Results.setText(_translate("MainWindow", "View Results"))
        self.actionGenerate.setText(_translate("MainWindow", "Generate"))
        self.actionImport_2.setText(_translate("MainWindow", "Import"))
        self.actionExport_2.setText(_translate("MainWindow", "Export"))
        self.actionScenario_Summary.setText(_translate("MainWindow", "Scenario Summary"))
        self.actionGenerate_2.setText(_translate("MainWindow", "Generate"))
        self.actionView_Results_2.setText(_translate("MainWindow", "View Results"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionAbout.setText(_translate("MainWindow", "About"))