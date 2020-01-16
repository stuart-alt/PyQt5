from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "PyQt5 Push Button"

        left = 500
        top = 200
        width = 300
        height = 250
        iconName = 'user.ico'

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("DON'T click me", self)
        # button.move(50, 50)
        button.setGeometry(QRect(100, 100, 151, 50))  # x and y position - then width and height
        button.setIcon(QtGui.QIcon("sair.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("IT DOESN'T DO ANYTHING!")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
