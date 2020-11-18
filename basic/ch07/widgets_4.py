import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
