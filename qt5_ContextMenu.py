from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QSizeGrip, \
    QFrame, QPushButton, QHBoxLayout, QSplitter, QLineEdit, QSlider, QLabel, QScrollArea, QFormLayout, QBoxLayout, \
    QGroupBox, QDial, QSpinBox, QDialog, QProgressBar, QToolBox, QMenuBar, QAction, QTextEdit, QFontDialog, QColorDialog, \
    QFileDialog, QMessageBox, QMenu
import sys
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QIcon, QActionEvent
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Context Menu"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def contextMenuEvent(self, event):
        contextMenu = QMenu()

        newAction = contextMenu.addAction("New")
        openAction = contextMenu.addAction("Open")
        quitAction = contextMenu.addAction("Quit")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
