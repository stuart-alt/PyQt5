from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Personalizando o PushButton"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("user.ico"))
        button = QPushButton("Salvar", self)
        button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: white; font: bold; border: none}')
        button.setToolTip("Clique para salvar os dados")
        button.move(200, 200)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
