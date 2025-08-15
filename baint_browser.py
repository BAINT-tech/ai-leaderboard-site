import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

# BaintBrowser - A simple web browser built with Python and PyQt5.

class BaintBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.setWindowTitle("BaintBrowser")
        self.setGeometry(100, 100, 1200, 800) # x, y, width, height

        # --- UI Components ---
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL and press Enter")

        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("http://example.com")) # Load a default page

        # --- Layout ---
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.address_bar)
        layout.addWidget(self.web_view)

        # --- Central Widget ---
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # --- Connections ---
        self.address_bar.returnPressed.connect(self.navigate_to_url)

    def navigate_to_url(self):
        url_text = self.address_bar.text()

        # Prepend "http://" if no scheme is present
        if not url_text.startswith(('http://', 'https://')):
            url_text = 'http://' + url_text

        self.web_view.setUrl(QUrl(url_text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BaintBrowser()
    browser.show()
    sys.exit(app.exec_())
