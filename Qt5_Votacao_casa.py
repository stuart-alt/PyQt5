from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QMessageBox, QAction, QRadioButton, \
    QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QDialog, QTableView
from PyQt5.QtCore import QCoreApplication
import mysql.connector
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQueryModel, QSqlQuery


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 - Votação"
        self.top = 400
        self.left = 100
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("_imagens/stuart.ico"))

        self.mainbox = QVBoxLayout()

        self.genderGroupBox = QGroupBox("Selecione o seu sexo")
        self.mainbox.addWidget(self.genderGroupBox)
        self.buttonMale = QRadioButton("Masculino")
        self.buttonMale.setIcon(QtGui.QIcon("_imagens/male.ico"))
        self.buttonMale.setIconSize(QtCore.QSize(30,30))
        self.buttonMale.setFont(QtGui.QFont("Sanserif", 13))

        self.buttonFemale = QRadioButton("Feminino")
        self.buttonFemale.setIcon(QtGui.QIcon("_imagens/female.png"))
        self.buttonFemale.setIconSize(QtCore.QSize(30, 30))
        self.buttonFemale.setFont(QtGui.QFont("Sanserif", 13))

        self.buttonNone = QRadioButton("Não informado")
        self.buttonNone.setIcon(QtGui.QIcon("_imagens/none.png"))
        self.buttonNone.setIconSize(QtCore.QSize(30, 30))
        self.buttonNone.setFont(QtGui.QFont("Sanserif", 13))

        self.genderButtonBox = QHBoxLayout()
        self.genderButtonBox.addWidget(self.buttonMale)
        self.genderButtonBox.addWidget(self.buttonFemale)
        self.genderButtonBox.addWidget(self.buttonNone)
        self.genderGroupBox.setLayout(self.genderButtonBox)

        self.sportsGroupBox = QGroupBox("Selecione o seu esporte favorito")
        self.mainbox.addWidget(self.sportsGroupBox)
        self.buttonSoccer = QRadioButton("Soccer")
        self.buttonSoccer.setIcon(QtGui.QIcon("_imagens/soccer.png"))
        self.buttonSoccer.setIconSize(QtCore.QSize(30, 30))
        self.buttonSoccer.setFont(QtGui.QFont("Sanserif", 13))

        self.buttonNFL = QRadioButton("NFL")
        self.buttonNFL.setIcon(QtGui.QIcon("_imagens/nfl.png"))
        self.buttonNFL.setIconSize(QtCore.QSize(30, 30))
        self.buttonNFL.setFont(QtGui.QFont("Sanserif", 13))

        self.buttonNBA = QRadioButton("NBA")
        self.buttonNBA.setIcon(QtGui.QIcon("_imagens/nba.png"))
        self.buttonNBA.setIconSize(QtCore.QSize(30, 30))
        self.buttonNBA.setFont(QtGui.QFont("Sanserif", 13))

        self.sportsButtonBox = QHBoxLayout()
        self.sportsButtonBox.addWidget(self.buttonSoccer)
        self.sportsButtonBox.addWidget(self.buttonNFL)
        self.sportsButtonBox.addWidget(self.buttonNBA)
        self.sportsGroupBox.setLayout(self.sportsButtonBox)

        self.choiceGroupBox = QGroupBox("Selecione uma opção")
        self.mainbox.addWidget(self.choiceGroupBox)
        self.okButton = QPushButton("Votar")
        self.okButton.clicked.connect(self.confirm_vote)
        self.okButton.setMaximumSize(QtCore.QSize(200, 50))
        self.closeButton = QPushButton("Fechar")
        self.closeButton.clicked.connect(self.close_app)
        self.closeButton.setMaximumSize(QtCore.QSize(200, 50))

        self.choiceButtonBox = QHBoxLayout()
        self.choiceButtonBox.addWidget(self.okButton)
        self.choiceButtonBox.addWidget(self.closeButton)
        self.choiceGroupBox.setLayout(self.choiceButtonBox)

        self.setLayout(self.mainbox)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def confirm_vote(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="Stuart",
            passwd="Stuart@2812",
            database="pyqt5"
        )
        mycursor = mydb.cursor()

        if self.buttonMale.isChecked() and self.buttonSoccer.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("1", "M")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonMale.isChecked() and self.buttonNFL.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("2", "M")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonMale.isChecked() and self.buttonNBA.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("3", "M")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonFemale.isChecked() and self.buttonSoccer.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("1", "F")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonFemale.isChecked() and self.buttonNFL.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("2", "F")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonFemale.isChecked() and self.buttonNBA.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("3", "F")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonNone.isChecked() and self.buttonSoccer.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("1", "N")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonNone.isChecked() and self.buttonNFL.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("2", "N")
            mycursor.execute(sql, val)
            mydb.commit()

        if self.buttonNone.isChecked() and self.buttonNBA.isChecked():
            sql = "INSERT INTO VOTOS (FK_ESPORTE, SEXO) VALUES (%s, %s)"
            val = ("3", "N")
            mycursor.execute(sql, val)
            mydb.commit()

        self.close_app()

    def show_popup(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="Stuart",
            passwd="Stuart@2812",
            database="pyqt5"
        )
        mycursor = mydb.cursor()

        qry = QSqlQuery()
        sql = """SELECT E.ESPORTE, SUM(V.FK_ESPORTE) AS "TOTAL VOTOS"
        FROM ESPORTES E
        INNER JOIN VOTOS V
        ON E.ID = V.FK_ESPORTE
        GROUP BY V.FK_ESPORTE;"""

        model = QSqlQueryModel()
        model.setQuery(sql)

        view = QTableView()
        view.setModel(model)

        view.show()

        """mycursor.execute(sql)
        resultado = mycursor.fetchall()
        print(resultado)"""


        """msg = QMessageBox()
        msg.setWindowTitle("Votos até o momento")
        msg.setText(resultado)

        x = msg.exec_()"""

    def close_app(self):
        self.show_popup()
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
