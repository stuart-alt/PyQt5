from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Frames"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color:lightgray')

        hbox = QHBoxLayout()

        btn = QPushButton("click me")
        btn.setStyleSheet('color:white')
        btn.setStyleSheet('background-color:green')

        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color:lightblue")
        frame.setLineWidth(0.6)

        hbox.addWidget(frame)
        hbox.addWidget(btn)
        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
