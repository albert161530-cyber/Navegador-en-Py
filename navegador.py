import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Navegador(QMainWindow):

    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.setCentralWidget(self.browser)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        back_btn = QAction("Atrás", self)
        back_btn.triggered.connect(self.browser.back)
        toolbar.addAction(back_btn)

        forward_btn = QAction("Adelante", self)
        forward_btn.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_btn)

        reload_btn = QAction("Recargar", self)
        reload_btn.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        self.setWindowTitle("Mi Navegador")
        self.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Mi Navegador")

window = Navegador()
app.exec_()