from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView
from PyQt5.QtCore import QCoreApplication
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class First(QWidget):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.title = "PyQt5 - Votação"
        self.top = 400
        self.left = 100
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("_imagens/stuart.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        vbox = QVBoxLayout()

        self.pushButton = QPushButton("click me")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

        vbox.addWidget(self.pushButton)

        self.setLayout(vbox)

        self.show()

    def on_pushButton_clicked(self):
        self.dialog.show()


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

        self.title = "PyQt5 - Resultado"
        self.top = 400
        self.left = 100
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("_imagens/stuart.ico"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        vbox2 = QVBoxLayout()
        self.btn = QPushButton("OK")
        self.btn.clicked.connect(self.fechar)
        vbox2.addWidget(self.btn)

        self.setLayout(vbox2)

        # self.show()

    def fechar(self):
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = First()
    sys.exit(App.exec_())
