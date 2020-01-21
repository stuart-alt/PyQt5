from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial, QSpinBox, QDialog, QProgressBar
import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1
            time.sleep(0.1)
            self.change_value.emit(cnt)


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QSpinBox"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.InitUI()

        self.show()

    def InitUI(self):
        vbox = QVBoxLayout()

        self.progressbar = QProgressBar()
        # self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 8px; padding: 1px}"
        #                               "QProgressBar::chunk {background:red}")
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setTextVisible(True)  # ou False
        self.progressbar.setMaximum(100)
        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Run progressbar")
        self.button.clicked.connect(self.startProgressBar)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
