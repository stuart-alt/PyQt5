from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Add Images"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 300
        self.iconName = "_imagens/mouse.ico"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("_imagens/books.jpg")
        labelImage.setPixmap(pixmap)

        vbox.addWidget(labelImage)
        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
