# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(716, 553)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblStatus = QtWidgets.QLabel(Dialog)
        self.lblStatus.setObjectName("lblStatus")
        self.verticalLayout_2.addWidget(self.lblStatus)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblCPU = QtWidgets.QLabel(Dialog)
        self.lblCPU.setObjectName("lblCPU")
        self.horizontalLayout_6.addWidget(self.lblCPU)
        self.lblMemory = QtWidgets.QLabel(Dialog)
        self.lblMemory.setObjectName("lblMemory")
        self.horizontalLayout_6.addWidget(self.lblMemory)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblGen = QtWidgets.QLabel(Dialog)
        self.lblGen.setObjectName("lblGen")
        self.horizontalLayout_2.addWidget(self.lblGen)
        self.lblFit = QtWidgets.QLabel(Dialog)
        self.lblFit.setObjectName("lblFit")
        self.horizontalLayout_2.addWidget(self.lblFit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnStop = QtWidgets.QPushButton(Dialog)
        self.btnStop.setObjectName("btnStop")
        self.verticalLayout_4.addWidget(self.btnStop)
        self.btnPause = QtWidgets.QPushButton(Dialog)
        self.btnPause.setObjectName("btnPause")
        self.verticalLayout_4.addWidget(self.btnPause)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.cmbSections = QtWidgets.QComboBox(Dialog)
        self.cmbSections.setObjectName("cmbSections")
        self.cmbSections.addItem("")
        self.horizontalLayout_7.addWidget(self.cmbSections)
        self.checkPreview = QtWidgets.QCheckBox(Dialog)
        self.checkPreview.setObjectName("checkPreview")
        self.horizontalLayout_7.addWidget(self.checkPreview)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tableSchedule = QtWidgets.QTableView(Dialog)
        self.tableSchedule.setObjectName("tableSchedule")
        self.verticalLayout_5.addWidget(self.tableSchedule)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate"))
        self.lblStatus.setText(_translate("Dialog", "Status:"))
        self.lblCPU.setText(_translate("Dialog", "CPU Usage:"))
        self.lblMemory.setText(_translate("Dialog", "Memory Usage:"))
        self.lblGen.setText(_translate("Dialog", "Generations:"))
        self.lblFit.setText(_translate("Dialog", "Average Fitness"))
        self.btnStop.setText(_translate("Dialog", "Stop Generation"))
        self.btnPause.setText(_translate("Dialog", "Pause Generation"))
        self.cmbSections.setCurrentText(_translate("Dialog", "Section 1"))
        self.cmbSections.setItemText(0, _translate("Dialog", "Section 1"))
        self.checkPreview.setText(_translate("Dialog", "Disable Preview"))

