from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Meu primeiro formulario em PyQt5"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 500
        self.setWindowIcon(QtGui.QIcon("user.ico"))

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
