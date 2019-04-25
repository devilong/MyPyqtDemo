# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browserform.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from tools.picmanager import PICManager
from PyQt5 import QtWebKitWidgets

class Ui_BrowserForm(object):
    def setupUi(self, BrowserForm):
        BrowserForm.setObjectName("BrowserForm")
        BrowserForm.resize(1000, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(BrowserForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(BrowserForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_back = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(PICManager.resource_path("resources/back.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.pushButton_next = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_next.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(PICManager.resource_path("resources/next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next.setIcon(icon1)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.pushButton_refresh = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_refresh.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(PICManager.resource_path("resources/refresh.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refresh.setIcon(icon2)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout.addWidget(self.pushButton_refresh)
        self.pushButton_homepage = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_homepage.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(PICManager.resource_path("resources/home.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_homepage.setIcon(icon3)
        self.pushButton_homepage.setObjectName("pushButton_homepage")
        self.horizontalLayout.addWidget(self.pushButton_homepage)
        self.lineEdit_url = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_url.setFont(font)
        self.lineEdit_url.setText("")
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.webView = QtWebKitWidgets.QWebView(BrowserForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl("file:///D:/PythonProject/SuperGenius/TeachDemo/render.html"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(BrowserForm)
        QtCore.QMetaObject.connectSlotsByName(BrowserForm)

    def retranslateUi(self, BrowserForm):
        _translate = QtCore.QCoreApplication.translate
        BrowserForm.setWindowTitle(_translate("BrowserForm", "网页浏览器"))


