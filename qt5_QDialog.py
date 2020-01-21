from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QButtonGroup, QHBoxLayout, \
    QLabel, QVBoxLayout, QGroupBox, QRadioButton, QDialog
import sys
from PyQt5 import QtGui, QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - QDialog @ stu_dados"
        self.top = 500
        self.left = 500
        self.width = 500
        self.height = 200
        self.iconName = "_imagens/stuart.ico"

        self.InitUI()

    def InitUI(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.btn = QPushButton("Open new window")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.openNewWindow)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()

    def openNewWindow(self):
        mydialog = QDialog(self)
        #mydialog.setModal(True)
        #mydialog.exec()

        mydialog.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
