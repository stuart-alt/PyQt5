import sys, sqlite3,  time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QComboBox, QBoxLayout, QGridLayout, QDialog, QWidget, \
    QPushButton, QApplication, QMainWindow, QAction, QMessageBox, QLabel, QTextEdit, QProgressBar, QLineEdit
from PyQt5.QtCore import QCoreApplication



class DBHelper():
    def __init__(self):
        self.conn=sqlite3.connect("sdms.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER, name TEXT, gender INTEGER, branch INTERGER, year INTERGER, academic year INTERGER, address TEXT, mobile INTERGER)")
        self.c.execute("CREATE TABLE IF NOT EXISTS payments(receipt_no INTEGER, roll INTEGER, fee INTEGER, semester INTEGER, receipt_date TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS genders(id INTEGER, name TEXT)")
        self.c.execute("CREATE TABLE IF NOT EXISTS branches(id INTEGER, name TEXT)")
    def addStudent(self, roll, name, gender, branch, year, academic_year, address, mobile):
        try:
            self.c.execute("INSERT INTO students(roll, name, gender, branch, year, academic_year, address, mobile) VALUES (?,?,?,?,?,?,?,?)", (roll, name, gender, branch, year, academic_year, address, mobile))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'stu_dados', 'Dados salvos com sucesso!')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'stu_dados', 'Não foi possível salvar os dados!')

    def searchStudent(self, roll):

        self.c.execute("SELECT * FROM students WHERE roll = " + str(roll))
        self.data=self.c.fetchone()


        if not self.data:
            QMessageBox.warning(QMessageBox(), 'stu_dados', 'Não foi possível encontrar a matricula!' + str(roll))
            return None
        self.list=[]
        for i in range(0, 8):
            self.list.append(self.data[i])
        self.c.close()
        self.conn.close()

        showStudent(self.list)




    def addPayment(self, roll, fee, semester):
        receipt_no=int(time.time())
        date=time.strftime("%b %d %y %H:%M:%S")
        try:


            self.c.execute("SELECT * FROM payments WHERE roll = " + str(roll))
            self.conn.commit()

            if not self.c.fetchone():

                if semester==1:

                    self.c.execute("SELECT * FROM payments WHERE roll = " + str(roll) + "AND semester = 0")


                    if not self.c.fetchone():
                        QMessageBox.warning(QMessageBox(), 'stu_dados', 'Estudante com a matricula ' + str(roll) + 'possui parcelas atrasadas')


                        return None
                else:
                    self.c.execute("INSERT INTO payments(receipt_no, roll, fee, semester, receipt_date)  VALUES(?,?,?,?,?)"), (receipt_no, roll, fee, semester, date)
                    self.conn.commit()
                    QMessageBox.information(QMessageBox(), 'stu_dados', 'Pagamento feito com sucesso! \ Referencia ID=' + str(receipt_no))

            else:


                self.c.execute("SELECT * FROM payments WHERE roll=" + str(roll))

                #we fetch all records
                self.data = self.c.fetchall()


                if len(self.data) == 2:
                    QMessageBox.warning(QMessageBox(), 'stu_dados', 'Estudante com a matricula' + str(roll) + 'fez o pagamento de duas parcelas')

                elif semester == 1:
                    self.c.execute("SELECT * FROM payments WHERE roll=" + str(roll) + "AND semester = 0")
                    if not self.c.fetchone():
                        QMessageBox.warning(QMessageBox(), 'stu_dados', 'Estudante com a matricula ' + str(roll) + 'tem parcelas para pagar')
                    else:
                        self.c.execute("INSERT INTO payments(receipt_no, roll, fee, semester, receipt_date)  VALUES(?,?,?,?,?)"), (receipt_no, roll, fee, semester, date)
                        self.conn.commit()
                        QMessageBox.information(QMessageBox(), 'stu_dados', 'Pagamento feito com sucesso! \ Referencia ID=' + str(receipt_no))






                elif self.data[0][3] == semester:
                    QMessageBox.information(QMessageBox(), 'stu_dados', 'Estudante com a matricula ' + str(roll) + 'ja pagou este semester')

                else:
                    self.c.execute("INSERT INTO payments(receipt_no, roll, fee, semester, receipt_date)  VALUES(?,?,?,?,?)"), (receipt_no, roll, fee, semester, date)


                    self.conn.commit()
                    QMessageBox.information(QMessageBox(), 'Pagamento feito com sucesso! \ Referencia ID=' + str(receipt_no))



        except Exception:
            QMessageBox.warning(QMessageBox(), 'stu_dados', 'Não foi possível realizar o pagamento')

        self.c.close()
        self.conn.close()
