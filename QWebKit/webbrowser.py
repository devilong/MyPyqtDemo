from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from apps.webbrowser.ui_browserform import Ui_BrowserForm
import sys

###############################################################################################
#######网页浏览器界面
###############################################################################################
class browserwindow(QtWidgets.QDialog, Ui_BrowserForm):
    def __init__(self, parent=None):
        super(browserwindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        #self.setFixedSize(self.width(), self.height())
        #self.showMaximized()
        #self.webView.setl
        self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.webView.page().linkClicked.connect(self.open_web)
        self.webView.urlChanged.connect(self.renew_urlbar)
        self.lineEdit_url.returnPressed.connect(self.on_pushButton_go_clicked)
        self.renew_pushButton()

        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        #QWebSettings.globalSettings().setAttribute(QWebSettings.JavascriptEnabled, True)
        #QWebSettings.globalSettings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        #QWebSettings.globalSettings().setAttribute(QWebSettings.JavascriptCanOpenWindows, True)

        #self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        #self.webView.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
        #self.webView.settings().setAttribute(QWebSettings.JavascriptCanCloseWindows, True)
        #self.webView.settings().setAttribute(QWebSettings.JavascriptCanOpenWindows, True)
        #self.webView.settings().setAttribute(QWebSettings.JavascriptCanAccessClipboard, True)
        #self.webView.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        #self.webView.settings().setAttribute(QWebSettings.SpatialNavigationEnabled, True)
        #self.webView.settings().setAttribute(QWebSettings.LinksIncludedInFocusChain, True)
        #self.webView.settings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)
        #self.webView.settings().setAttribute(QWebSettings.AutoLoadImages, True)

        # self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
   ########################################################################
    #回退按钮
    @pyqtSlot()
    def on_pushButton_back_clicked(self):
        page = self.webView.page()
        history = page.history()
        history.back()
        self.renew_pushButton()


    #前进按钮
    @pyqtSlot()
    def on_pushButton_next_clicked(self):
        page = self.webView.page()
        history = page.history()
        history.forward()
        self.renew_pushButton()



    #刷新按钮
    @pyqtSlot()
    def on_pushButton_refresh_clicked(self):
        url = QUrl(self.lineEdit_url.text())
        self.open_web(url)

    #主页按钮
    @pyqtSlot()
    def on_pushButton_homepage_clicked(self):
        self.homepage_url = "www.baidu.com"
        url = QUrl(self.homepage_url)
        self.open_web(url)

    # 浏览按钮
    @pyqtSlot()
    def on_pushButton_go_clicked(self):
        url = QUrl(self.lineEdit_url.text())
        self.open_web(url)

    # 打开网页
    def open_web(self,url):
        if url.scheme() == '':
            url.setScheme('https')
        self.webView.setUrl(url)

    #刷新按钮
    def renew_pushButton(self):
        page = self.webView.page()
        history = page.history()
        if history.canGoBack():
            self.pushButton_back.setEnabled(True)
        else:
            self.pushButton_back.setEnabled(False)
        if history.canGoForward():
            self.pushButton_next.setEnabled(True)
        else:
            self.pushButton_next.setEnabled(False)

    #刷新地址栏
    def renew_urlbar(self, qurl):
        self.lineEdit_url.setText(qurl.url())
        self.lineEdit_url.setCursorPosition(0)
        self.renew_pushButton()




####################################
#程序入口
####################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.addLibraryPath("./plugins")
    theshow = browserwindow()
    theshow.show()
    sys.exit(app.exec_())