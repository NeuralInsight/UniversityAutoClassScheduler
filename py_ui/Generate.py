# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_ui/generate_fa.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(997, 818)
        Dialog.setMinimumSize(QtCore.QSize(716, 553))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnPause = QtWidgets.QPushButton(self.groupBox_4)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout_4.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.groupBox_4)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout_4.addWidget(self.btnStop)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cmbSection = QtWidgets.QComboBox(self.groupBox_3)
        self.cmbSection.setObjectName("cmbSection")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.cmbSection.addItem("")
        self.horizontalLayout_5.addWidget(self.cmbSection)
        self.chkPreview = QtWidgets.QCheckBox(self.groupBox_3)
        self.chkPreview.setObjectName("chkPreview")
        self.horizontalLayout_5.addWidget(self.chkPreview)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCPU = QtWidgets.QLabel(self.groupBox)
        self.lblCPU.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblCPU.setObjectName("lblCPU")
        self.gridLayout_2.addWidget(self.lblCPU, 2, 0, 1, 1)
        self.lblTime = QtWidgets.QLabel(self.groupBox)
        self.lblTime.setObjectName("lblTime")
        self.gridLayout_2.addWidget(self.lblTime, 0, 0, 1, 2)
        self.lblMemory = QtWidgets.QLabel(self.groupBox)
        self.lblMemory.setObjectName("lblMemory")
        self.gridLayout_2.addWidget(self.lblMemory, 2, 1, 1, 1)
        self.lblStatus = QtWidgets.QLabel(self.groupBox)
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout_2.addWidget(self.lblStatus, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.boxGen = QtWidgets.QGroupBox(Dialog)
        self.boxGen.setObjectName("boxGen")
        self.gridLayout = QtWidgets.QGridLayout(self.boxGen)
        self.gridLayout.setObjectName("gridLayout")
        self.lblFitness = QtWidgets.QLabel(self.boxGen)
        self.lblFitness.setObjectName("lblFitness")
        self.gridLayout.addWidget(self.lblFitness, 2, 0, 1, 1)
        self.lblPreviousFitness = QtWidgets.QLabel(self.boxGen)
        self.lblPreviousFitness.setObjectName("lblPreviousFitness")
        self.gridLayout.addWidget(self.lblPreviousFitness, 2, 1, 1, 1)
        self.lblPopulation = QtWidgets.QLabel(self.boxGen)
        self.lblPopulation.setObjectName("lblPopulation")
        self.gridLayout.addWidget(self.lblPopulation, 1, 0, 1, 1)
        self.lblMutation = QtWidgets.QLabel(self.boxGen)
        self.lblMutation.setObjectName("lblMutation")
        self.gridLayout.addWidget(self.lblMutation, 1, 1, 1, 1)
        self.lblHighestFitness = QtWidgets.QLabel(self.boxGen)
        self.lblHighestFitness.setObjectName("lblHighestFitness")
        self.gridLayout.addWidget(self.lblHighestFitness, 3, 0, 1, 1)
        self.lblLowestFitness = QtWidgets.QLabel(self.boxGen)
        self.lblLowestFitness.setObjectName("lblLowestFitness")
        self.gridLayout.addWidget(self.lblLowestFitness, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.boxGen)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.tableSchedule = QtWidgets.QTableView(Dialog)
        self.tableSchedule.setObjectName("tableSchedule")
        self.verticalLayout_5.addWidget(self.tableSchedule)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(0, 60, 981, 31))
        self.progressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lblProgressStatus = QtWidgets.QLabel(self.groupBox_2)
        self.lblProgressStatus.setGeometry(QtCore.QRect(10, 30, 951, 20))
        self.lblProgressStatus.setObjectName("lblProgressStatus")
        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate"))
        self.groupBox_4.setTitle(_translate("Dialog", "عملیات"))
        self.btnPause.setText(_translate("Dialog", "متوقف کردن اجرا"))
        self.btnStop.setText(_translate("Dialog", "پایان اجرا"))
        self.groupBox_3.setTitle(_translate("Dialog", "پیش نمایش"))
        self.cmbSection.setItemText(0, _translate("Dialog", "Section 1"))
        self.cmbSection.setItemText(1, _translate("Dialog", "Section 2"))
        self.cmbSection.setItemText(2, _translate("Dialog", "Section 3"))
        self.cmbSection.setItemText(3, _translate("Dialog", "Section 4"))
        self.cmbSection.setItemText(4, _translate("Dialog", "Section 5"))
        self.chkPreview.setText(_translate("Dialog", "غیرفعال کردن پیش نمایش"))
        self.groupBox.setTitle(_translate("Dialog", "وضعیت سیستم"))
        self.lblCPU.setText(_translate("Dialog", "پردازنده:"))
        self.lblTime.setText(_translate("Dialog", "زمان سپری شده: "))
        self.lblMemory.setText(_translate("Dialog", "حافظه رم :‌ "))
        self.lblStatus.setText(_translate("Dialog", "وضعیت: "))
        self.boxGen.setTitle(_translate("Dialog", "نسل"))
        self.lblFitness.setText(_translate("Dialog", "میانگین فیتنس:"))
        self.lblPreviousFitness.setText(_translate("Dialog", "میانگین فیتنس نسل قبل:"))
        self.lblPopulation.setText(_translate("Dialog", "جمعیت :‌"))
        self.lblMutation.setText(_translate("Dialog", "نرخ فعلی جهش:‌ "))
        self.lblHighestFitness.setText(_translate("Dialog", "بالاترین فیتنس:"))
        self.lblLowestFitness.setText(_translate("Dialog", "پایین ترین فیتنس:"))
        self.groupBox_2.setTitle(_translate("Dialog", "پیشروی الگوریتم"))
        self.lblProgressStatus.setText(_translate("Dialog", "مرحله: "))