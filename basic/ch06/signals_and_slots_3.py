import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
    'My App',
    'Still My App',
    'What on earth',
    'This is suprising',
    'Something went wrong'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0
        self.setWindowTitle('My App')
        self.button = QPushButton('Push Me!')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print('Clicked')
        new_window_title = random.choice(window_titles)
        print('Setting title: %s' % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print('Window title chagned: %s' % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
