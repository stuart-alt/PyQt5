from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, \
    QRadioButton, QLabel
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
import mysql.connector
from PyQt5.QtCore import Qt


mydb = mysql.connector.connect(
    host="localhost",
    user="stuart",
    passwd="Stuart@2812",
    database="pyqt5"
)

#print(mydb)

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Layout"
        self.left = 500
        self.top = 200
        self.width = 200
        self.height = 200
        self.iconName = "_imagens/mouse.ico"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox1)
        vbox.addWidget(self.groupBox2)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox1 = QGroupBox("Selecione o seu gênero")
        self.groupBox1.setAlignment(Qt.AlignCenter)
        hbox1layout = QHBoxLayout()

        self.radiobuttonMasculino = QRadioButton("Masculino")
        self.radiobuttonMasculino.setChecked(True)
        self.radiobuttonMasculino.gender = "M"
        hbox1layout.addWidget(self.radiobuttonMasculino)

        self.radiobuttonFemino = QRadioButton("Feminino")
        self.radiobuttonFemino.gender = "F"
        hbox1layout.addWidget(self.radiobuttonFemino)

        self.radiobuttonNone = QRadioButton("Não informado")
        self.radiobuttonNone.gender = "N"
        hbox1layout.addWidget(self.radiobuttonNone)

        self.groupBox2 = QGroupBox("Selecione o seu esporte favorito")
        self.groupBox2.setAlignment(Qt.AlignCenter)
        hbox2layout = QHBoxLayout()

        buttonSoccer = QPushButton("Soccer", self)
        buttonSoccer.setIcon(QtGui.QIcon("_imagens/soccer.png"))
        buttonSoccer.setIconSize(QtCore.QSize(20, 20))
        buttonSoccer.setMinimumHeight(40)
        hbox2layout.addWidget(buttonSoccer)
        buttonSoccer.clicked.connect(self.clickSoccer)

        buttonBaseball = QPushButton("Baseball", self)
        buttonBaseball.setIcon(QtGui.QIcon("_imagens/baseball.png"))
        buttonBaseball.setIconSize(QtCore.QSize(20, 20))
        buttonBaseball.setMinimumHeight(40)
        hbox2layout.addWidget(buttonBaseball)
        buttonBaseball.clicked.connect(self.clickBaseball)

        buttonTennis = QPushButton("Tennis", self)
        buttonTennis.setIcon(QtGui.QIcon("_imagens/tennis.jpg"))
        buttonTennis.setIconSize(QtCore.QSize(20, 20))
        buttonTennis.setMinimumHeight(40)
        hbox2layout.addWidget(buttonTennis)
        buttonTennis.clicked.connect(self.clickTennis)

        self.groupBox1.setLayout(hbox1layout)
        self.groupBox2.setLayout(hbox2layout)

    def clickSoccer(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO votos (id_esporte, sexo) VALUES (%s, %s)"
        if self.radiobuttonMasculino.isChecked():
            gender = self.radiobuttonMasculino.gender
        elif self.radiobuttonFemino.isChecked():
            gender = self.radiobuttonFemino.gender
        else:
            gender = self.radiobuttonNone.gender
        val = (1, gender)
        mycursor.execute(sql, val)
        mydb.commit()
        self.showResult()

    def clickBaseball(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO votos (id_esporte, sexo) VALUES (%s, %s)"
        if self.radiobuttonMasculino.isChecked():
            gender = self.radiobuttonMasculino.gender
        elif self.radiobuttonFemino.isChecked():
            gender = self.radiobuttonFemino.gender
        else:
            gender = self.radiobuttonNone.gender
        val = (2, gender)
        mycursor.execute(sql, val)
        mydb.commit()
        self.showResult()

    def clickTennis(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO votos (id_esporte, sexo) VALUES (%s, %s)"
        if self.radiobuttonMasculino.isChecked():
            gender = self.radiobuttonMasculino.gender
        elif self.radiobuttonFemino.isChecked():
            gender = self.radiobuttonFemino.gender
        else:
            gender = self.radiobuttonNone.gender
        val = (3, gender)
        mycursor.execute(sql, val)
        mydb.commit()
        self.showResult()

    def showResult(self):
        vbox3 = QVBoxLayout()
        mycursor = mydb.cursor()
        sql = """SELECT E.ESPORTE, 
        COUNT(CASE WHEN V.SEXO = "M" THEN V.SEXO END) AS 'MASCULINO',
        COUNT(CASE WHEN V.SEXO = "F" THEN V.SEXO END) AS 'FEMININO',
        COUNT(CASE WHEN V.SEXO = "N" THEN V.SEXO END) AS 'NÃO INFORMADO',
        COUNT(*) AS TOTAL
        FROM ESPORTES E 
        INNER JOIN VOTOS V 
        ON E.ID = V.ID_ESPORTE
        GROUP BY E.ESPORTE;"""

        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        label = QLabel(mycursor)
        vbox3.addWidget(label)

        self.setLayout(vbox3)

        self.show()

        #sys.exit(App.exec())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
