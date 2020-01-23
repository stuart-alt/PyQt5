from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView, QStackedWidget, QLabel
from PyQt5.QtCore import QCoreApplication
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class StackWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Stacked Widgets"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.StackedWidget()

        self.show()

    def StackedWidget(self):
        vbox = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        vbox.addWidget(self.stackedWidget)

        for x in range(0, 8):
            label = QLabel("Stacked Child" + str(x))
            label.setFont(QtGui.QFont("Sanserif", 15))
            label.setStyleSheet('color:red')

            self.stackedWidget.addWidget(label)

            self.button = QPushButton("Stack " + str(x))
            self.button.setStyleSheet('background-color:green')
            self.button.page = x

            self.button.clicked.connect(self.btn_clicked)

            vbox.addWidget(self.button)
        self.setLayout(vbox)

    def btn_clicked(self):
        self.button = self.sender()
        self.stackedWidget.setCurrentIndex(self.button.page)





if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = StackWidget()
    sys.exit(App.exec())
