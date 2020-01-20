from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, \
    QGridLayout, QLabel
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Labels"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        label = QLabel("This is Qt5 label")
        vbox.addWidget(label)

        label2 = QLabel("This is Qt5 GUI App Development")
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet('color:blue')
        vbox.addWidget(label2)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
