from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QButtonGroup, QHBoxLayout, \
    QLabel, QVBoxLayout, QGroupBox, QRadioButton, QTableWidget, QTableView
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import ast


def MyConverter(mydata):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)
    return tuple(map(cvt, mydata))


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QButton Group @ stu_dados"
        self.top = 500
        self.left = 500
        self.width = 500
        self.height = 200
        self.iconName = "_imagens/stuart.ico"

        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def LoadData(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="Stuart",
            passwd="Stuart@2812",
            database="pyqt5"
        )
        mycursor = mydb.cursor()
        rows = mycursor.execute("""SELECT E.ESPORTE, SUM(V.FK_ESPORTE) AS "TOTAL VOTOS"
        FROM ESPORTES E
        INNER JOIN VOTOS V
        ON E.ID = V.FK_ESPORTE
        GROUP BY V.FK_ESPORTE;""")
        data = mycursor.fetchall()

        for rown in data:
            self.addTable()

    def addTable(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
