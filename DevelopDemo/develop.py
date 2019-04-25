import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('My Browser')
        self.showMaximized()

        self.webview = WebEngineView()
        self.webview.load(QUrl("https://www.baidu.com"))
        self.setCentralWidget(self.webview)

        runAction = QAction('Test', self)
        runAction.triggered.connect(self.testAjax)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbar.addAction(runAction)

    def testAjax(self):
        js_string = '''
                $.ajax({
                    url: 'http://www.baidu.com',
                    async:false,
                    success: function(re) {
                        return '111';
                    }
                })
        '''
        self.webview.page().runJavaScript(js_string, self.getTestAjax)

    def getTestAjax(self, re):
        print(re)







class WebEngineView(QWebEngineView):
    windowList = []

    # 重写createwindow()
    def createWindow(self, QWebEnginePage_WebWindowType):
        new_webview =   WebEngineView()
        new_window = MainWindow()
        new_window.setCentralWidget(new_webview)

        self.windowList.append(new_window)  #注：没有这句会崩溃！！！
        self.windowList[0].close()
        print(self.windowList)
        return new_webview


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())