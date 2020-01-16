from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QHBoxLayout, QLabel, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Qline edit @ stu_dados"
        self.top = 300
        self.left = 300
        self.width = 900
        self.height = 300
        self.iconName = "_imagens/stuart.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.OnPressed)
        hbox.addWidget(self.lineedit)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def OnPressed(self):
        self.label.setText(self.lineedit.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
