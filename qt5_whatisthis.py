from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow, QPushButton, QDialog, \
    QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, QWidget
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - what is this class @ stu_dados"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.iconName = "_imagens/stuart.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()
        label = QLabel("Focus and press SHIFT + F1")
        hbox.addWidget(label)

        button = QPushButton("CLICK ME", self)
        button.setWhatsThis("This is a button that you can click")
        hbox.addWidget(button)
        
        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
