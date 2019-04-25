# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'developform.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DevelopFormDialog(object):
    def setupUi(self, DevelopFormDialog):
        DevelopFormDialog.setObjectName("DevelopFormDialog")
        DevelopFormDialog.resize(875, 583)
        self.timeEdit = QtWidgets.QTimeEdit(DevelopFormDialog)
        self.timeEdit.setGeometry(QtCore.QRect(40, 80, 118, 22))
        self.timeEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(DevelopFormDialog)
        self.dateEdit.setGeometry(QtCore.QRect(40, 200, 110, 22))
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(DevelopFormDialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(30, 320, 194, 22))
        self.dateTimeEdit.setReadOnly(True)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(DevelopFormDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(540, 150, 296, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.timeEdit_2 = QtWidgets.QTimeEdit(DevelopFormDialog)
        self.timeEdit_2.setGeometry(QtCore.QRect(310, 80, 118, 22))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(DevelopFormDialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(310, 210, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(DevelopFormDialog)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(300, 330, 194, 22))
        self.dateTimeEdit_2.setReadOnly(True)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.retranslateUi(DevelopFormDialog)
        QtCore.QMetaObject.connectSlotsByName(DevelopFormDialog)

    def retranslateUi(self, DevelopFormDialog):
        _translate = QtCore.QCoreApplication.translate
        DevelopFormDialog.setWindowTitle(_translate("DevelopFormDialog", "Dialog"))

