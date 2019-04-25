# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *

################################################
#######创建主窗口
################################################
class AppWidget(QWidget):
    def __init__(self, parent=None):
        super(AppWidget, self).__init__(parent)
        self.setWindowTitle("界面风格例子")

        # 设置界面控件
        self.styleLabel = QLabel("Set Style:")
        self.styleComboBox = QComboBox()
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.styleLabel)
        self.horizontalLayout.addWidget(self.styleComboBox)


        # QComboBox初始化
        self.styleComboBox.addItems(QStyleFactory.keys())
        index = self.styleComboBox.findText(QApplication.style().objectName(),QtCore.Qt.MatchFixedString)
        self.styleComboBox.setCurrentIndex(index)

        # QComboBox点击触发
        self.styleComboBox.activated[str].connect(self.on_styleComboBox_Activate)



    def on_styleComboBox_Activate(self, style):
        QApplication.setStyle(style)


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widgetApp = AppWidget()
    widgetApp.show()
    sys.exit(app.exec_())

