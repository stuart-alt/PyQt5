from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView, QStackedWidget, QLabel, QDockWidget, QTextEdit, QListWidget
from PyQt5.QtCore import QCoreApplication, Qt
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class DockDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Dock Widget"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createDockWidget()

        self.show()

    def createDockWidget(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Close")

        self.dock = QDockWidget("Dockable", self)
        self.listwidget = QListWidget()
        list = ["python", "C++", "Javascript"]
        self.listwidget.addItems(list)
        self.dock.setWidget(self.listwidget)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = DockDialog()
    sys.exit(App.exec())
