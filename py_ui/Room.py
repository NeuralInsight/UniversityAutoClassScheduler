# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_ui/room_fa.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 655)
        # Dialog.setMinimumSize(QtCore.QSize(712, 657))
        # Dialog.setMaximumSize(QtCore.QSize(712, 657))
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioLec = QtWidgets.QRadioButton(self.groupBox)
        self.radioLec.setChecked(True)
        self.radioLec.setObjectName("radioLec")
        self.horizontalLayout_2.addWidget(self.radioLec)
        self.radioLab = QtWidgets.QRadioButton(self.groupBox)
        self.radioLab.setObjectName("radioLab")
        self.horizontalLayout_2.addWidget(self.radioLab)
        self.gridLayout.addWidget(self.groupBox, 0, 3, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblName = QtWidgets.QLabel(self.groupBox_2)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout_3.addWidget(self.lblName)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditName.setObjectName("lineEditName")
        self.horizontalLayout_3.addWidget(self.lineEditName)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableSchedule = QtWidgets.QTableView(Dialog)
        self.tableSchedule.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableSchedule.setObjectName("tableSchedule")
        self.tableSchedule.setMinimumSize(QtCore.QSize(694, 509))
        self.tableSchedule.setMaximumSize(QtCore.QSize(694, 509))
        self.verticalLayout.addWidget(self.tableSchedule)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnFinish = QtWidgets.QPushButton(Dialog)
        self.btnFinish.setObjectName("btnFinish")
        self.horizontalLayout.addWidget(self.btnFinish)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lblName.setBuddy(self.lineEditName)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditName, self.radioLec)
        Dialog.setTabOrder(self.radioLec, self.radioLab)
        Dialog.setTabOrder(self.radioLab, self.tableSchedule)
        Dialog.setTabOrder(self.tableSchedule, self.btnFinish)
        Dialog.setTabOrder(self.btnFinish, self.btnCancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Room"))
        self.groupBox.setTitle(_translate("Dialog", "نوع کلاس"))
        self.radioLec.setText(_translate("Dialog", "نظری"))
        self.radioLab.setText(_translate("Dialog", "عملی"))
        self.groupBox_2.setTitle(_translate("Dialog", "مشخصات"))
        self.lblName.setText(_translate("Dialog", "کد کلاس"))
        self.btnFinish.setText(_translate("Dialog", "ایجاد"))
        self.btnFinish.setShortcut(_translate("Dialog", "Ctrl+S"))
        self.btnCancel.setText(_translate("Dialog", "بستن"))