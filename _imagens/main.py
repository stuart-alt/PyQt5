import sys, sqlite3,  time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QComboBox, QBoxLayout, QGridLayout, QDialog, QWidget, \
    QPushButton, QApplication, QMainWindow, QAction, QMessageBox, QLabel, QTextEdit, QProgressBar, QLineEdit, QVBoxLayout
from PyQt5.QtCore import QCoreApplication


class DBHelper():
    def __init__(self):
        self.conn = sqlite3.connect("sdms.db")
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
                if semester == 1:
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

    def searchPayment(self, roll):
        self.c.execute("SELECT * FROM payments WHERE roll = " + str(roll) + "ORDER BY receipt_no DESC")
        self.data = self.c.fetchone()
        if not self.data:
            QMessageBox.warning(QMessageBox(), 'stu_dados', 'Não foi possível encontrar a matricula!' + str(roll))
            return None
        self.list = self.data
        self.c.close()
        self.conn.close()
        showPaymentFunction(self.list)


class Login(QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.userNameLabel = QLabel("USUARIO")
        self.userPassLabel = QLabel("SENHA")
        self.textName = QLineEdit(self)
        self.textPass = QLineEdit(self)
        self.buttonLogin = QPushButton('Entrar', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QGridLayout(self)
        layout.addWidget(self.userNameLabel, 1, 1)
        layout.addWidget(self.userPassLabel, 2, 1)
        layout.addWidget(self.textName, 1, 2)
        layout.addWidget(self.textPass, 2, 2)
        layout.addWidget(self.buttonLogin, 3, 1, 1, 2)
        self.setWindowTitle("Login")

    def handleLogin(self):
        if self.textName.text() == 'admin' and self.textPass() == 'admin':
            self.accept()
        else:
            QMessageBox.warning(self, 'stu_dados', 'Login não autorizado!')

    def showStudent(list):
        roll = 0
        gender = branch = year = name = address = ""
        mobile = academic_year = -1
        roll = list[0]
        name = list[1]

        if list[2] == 0:
            gender = "Masculino"
        else:
            gender = "Feminino"
        if list[3] == 0:
            branch = "Engenharia Mecaninca"
        elif list[3] == 1:
            branch = "Engenharia Civil"
        elif list[3] == 2:
            branch = "Engenharia Elétrica"
        elif list[3] == 3:
            branch = "Engenharia eletrônica e de cominucações"
        elif list[3] == 4:
            branch = "Ciência da Computação e Engenharia"
        elif list[3] == 5:
            branch = "Tecnologia da Informação"
        if list[4] == 0:
            year = "1"
        elif list[4] == 1:
            year = "2"
        elif list[4] == 2:
            year = "3"
        elif list[4] == 3:
            year = "4"

        academic_year = list[5]
        address = list[6]
        mobile = list[7]

        table = QTableWidget()
        tableItem = QTableWidgetItem()
        table.setWindowTitle("DETALHES DO ALUNO: ")
        table.setRowCount(8)
        table.setColumnCount(2)

        table.setItem(0, 0, QTableWidgetItem("Matricula: "))
        table.setItem(0, 1, QTableWidgetItem(str(roll)))
        table.setItem(1, 0, QTableWidgetItem("Nome: "))
        table.setItem(1, 1, QTableWidgetItem(str(name)))
        table.setItem(2, 0, QTableWidgetItem("Sexo: "))
        table.setItem(2, 1, QTableWidgetItem(str(gender)))
        table.setItem(3, 0, QTableWidgetItem("Filial: "))
        table.setItem(3, 1, QTableWidgetItem(str(branch)))
        table.setItem(4, 0, QTableWidgetItem("Ano: "))
        table.setItem(4, 1, QTableWidgetItem(str(year)))
        table.setItem(5, 0, QTableWidgetItem("Ano academico: "))
        table.setItem(5, 1, QTableWidgetItem(str(academic_year)))
        table.setItem(6, 0, QTableWidgetItem("Endereço: "))
        table.setItem(6, 1, QTableWidgetItem(str(address)))
        table.setItem(7, 0, QTableWidgetItem("Celular: "))
        table.setItem(7, 1, QTableWidgetItem(str(mobile)))

        table.horizontalHeader().setStretchLastSection(True)
        table.show()

        dialog = QDialog()
        dialog.setWindowTitle("DETALHES DO ALUNO: ")
        dialog.resize(500, 300)
        dialog.setLayout(QVBoxLayout())
        dialog.layout().addWidget(table)
        dialog.exec()

    def showPaymentFunction(list):
        roll = -1
        recipt_no = -1
        fee = -1
        semester = -1
        recipt_date = ""
        recipt_no = list[0]
        roll = list[1]
        fee = list[2]
        if list[3] == 0:
            semester = "Semestre atrasado"
        elif list[3] == 1:
            semester = "Voce deve pagar os dois semestres atrasados."
        recipt_date = list[4]

        table = QTableWidget()
        tableItem = QTableWidgetItem()
        table.setWindowTitle("DETALHES DOS PAGAMENTOS: ")
        table.setRowCount(5)
        table.setColumnCount(2)

        table.setItem(0, 0, QTableWidgetItem("Recibo: "))
        table.setItem(0, 1, QTableWidgetItem(str(recipt_no)))
        table.setItem(1, 0, QTableWidgetItem("Matricula: "))
        table.setItem(1, 1, QTableWidgetItem(str(roll)))
        table.setItem(2, 0, QTableWidgetItem("Total taxa: "))
        table.setItem(2, 1, QTableWidgetItem(str(fee)))
        table.setItem(3, 0, QTableWidgetItem("Semestre: "))
        table.setItem(3, 1, QTableWidgetItem(str(semester)))
        table.setItem(4, 0, QTableWidgetItem("Data Pagamento: "))
        table.setItem(4, 1, QTableWidgetItem(str(recipt_date)))

        table.horizontalHeader().setStretchLastSection(True)
        table.show()

        dialog = QDialog()
        dialog.setWindowTitle("DETALHES DOS PAGAMENTOS: ")
        dialog.resize(500, 300)
        dialog.setLayout(QVBoxLayout())
        dialog.layout().addWidget(table)
        dialog.exec()

class AddStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.gender = -1
        self.branch = -1
        self.year = -1
        self.roll = -1
        self.name = ""
        self.address = ""
        self.mobile = -1
        self.aself.cademic_year = -1

        self.btnCancelar = QPushButton("Cancelar", self)
        self.btnReset = QPushButton("Limpar", self)
        self.btnAdd = QPushButton("Adicionar", self)

        self.btnCancelar.setFixedHeight(30)
        self.btnReset.setFixedHeight(30)
        self.btnAdd.setFixedHeight(30)

        self.YearCombo = QComboBox(self)
        self.YearCombo.addItem("1")
        self.YearCombo.addItem("2")
        self.YearCombo.addItem("3")
        self.YearCombo.addItem("4")

        self.GenderCombo = QComboBox(self)
        self.GenderCombo.addItem("Masculino")
        self.GenderCombo.addItem("Feminino")

        self.BranchCombo = QComboBox(self)
        self.BranchCombo.addItem("Engenharia Mecaninca")
        self.BranchCombo.addItem("Engenharia Elétrica")
        self.BranchCombo.addItem("Engenharia eletrônica e de cominucações")
        self.BranchCombo.addItem("Ciência da Computação e Engenharia")
        self.BranchCombo.addItem("Tecnologia da Informação")

        self.rollLabel = QLabel("Matricula No")
        self.nameLabel = QLabel("Nome")
        self.addressLabel = QLabel("Endereco")
        self.mobLabel = QLabel("Mobile")
        self.yearLabel = QLabel("Ano Atual")
        self.academic_yearLabel("Ano Academico")
        self.branchLabel = QLabel("Filial")
        self.genderLabel = QLabel("Sexo")

        self.rollText = QLineEdit(self)
        self.nameText = QLineEdit(self)
        self.addressText = QLineEdit(self)
        self.mobText = QLineEdit(self)
        self.academic_yearText = QLineEdit(self)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.rollLabel, 1, 1)
        self.grid.addWidget(self.nameLabel, 2, 1)
        self.grid.addWidget(self.genderLabel, 3, 1)
        self.grid.addWidget(self.addressLabel, 4, 1)
        self.grid.addWidget(self.mobileLabel, 5, 1)
        self.grid.addWidget(self.branchLabel, 6, 1)
        self.grid.addWidget(self.yearLabel, 7, 1)
        self.grid.addWidget(self.academic_yearLabel, 8, 1)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.rollText, 1, 2)
        self.grid.addWidget(self.nameText, 2, 2)
        self.grid.addWidget(self.genderCombo, 3, 2)
        self.grid.addWidget(self.addressText, 4, 2)
        self.grid.addWidget(self.mobiletext, 5, 2)
        self.grid.addWidget(self.branchCombo, 6, 2)
        self.grid.addWidget(self.yearCombo, 7, 2)
        self.grid.addWidget(self.academic_yearText, 8, 2)

        self.grid.addWidget(self.btnReset, 9, 1)
        self.grid.addWidget(self.btnCancelar, 9, 2)
        self.grid.addWidget(self.btnAdd, 9,3)

        self.btnAdd.clicked.connect(self.addStudent)
        self.btnCancelar.clicked.connect(QApplication.instance().quit)
        self.btnReset.clicked.connect(self.reset)

        self.setLayout(self.grid)
        self.setWindowTitle("ADICIONAR DETALHES DO ESTUDANTE: ")
        self.resize(500, 300)
        self.show()
        sys.exit(self.exec_())

    def reset(self):
        self.rollText.setText("")
        self.nameText.setText("")
        self.academic_yearText.setText("")
        self.addressText.setText("")
        self.mobText.setText("")

    def addStudent(self):
        self.gender = self.genderCombo.currentIndex()
        self.year = self.yearCombo.currentIndex()
        self.branch = self.branchCombo.currentIndex()
        self.roll = int(self.rollText.text())
        self.name = self.nameText.text()
        self.academic_year = int(self.academic_yearText.text())
        self.address = self.addressText.text()
        self.mobile = int(self.mobileText.text())

        self.dbhelper = DBHelper()
        self.dbhelper.addStudent(self.roll, self.name, self.gender, self.branch, self.year,
                                 self.academic_year, self.address, self.mobile)


class AddPayment(QDialog):
    def __init__(self):
        super().__init__()
        self.receipt_no = -1
        self.roll = -1
        self.fee = -1
        self.semester = -1
        self.data = -1

        self.btnCancel = QPushButton("Cancelar", self)
        self.btnReset = QPushButton("Limpar", self)
        self.btnAdd = QPushButton("Adicionar", self)

        self.btnCancel.setFixedHeight(30)
        self.btnReset.setFixedHeight(30)
        self.btnAdd.setFixedHeight(30)

        self.semesterCombo = QComboBox(self)
        self.semesterCombo.addItem("Impar")
        self.semesterCombo.addItem("Par")

        self.rollLabel = QLabel("Matricula No")
        self.feeLabel = QLabel("total Taxa")
        self.semesterLabel = QLabel("Semester")

        self.rollText = QLineEdit(self)
        self.feeText = QLineEdit(self)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.rollLabel, 1, 1)
        self.grid.addWidget(self.feeLabel, 2, 1)
        self.grid.addWidget(self.semesterLabel, 3, 1)

        self.grid.addWidget(self.rollText, 1, 1)
        self.grid.addWidget(self.feeText, 2, 2)
        self.grid.addWidget(self.semesterCombo, 3, 2)

        self.grid.addWidget(self.btnReset, 4, 1)
        self.grid.addWidget(self.btnCancel, 4, 2)
        self.grid.addWidget(self.btnAdd, 4,3)

        self.btnAdd.clicked.connect(self.addPayment)
        self.btnCancelar.clicked.connect(QApplication.instance().quit)
        self.btnReset.clicked.connect(self.reset)

        self.setLayout(self.grid)
        self.setWindowTitle("ADICIONAR DETALHES DO PAGAMENTO: ")
        self.resize(500, 200)
        self.show()
        sys.exit(self.exec_())

    def reset(self):
        self.rollText.setText("")
        self.feeLabelText.setText("")

    def AddPayment(self):
        self.semester = self.semesterCombo.currentIndex()
        self.roll = int(self.rollText.text())
        self.fee = int(self.feeLabelText.text())

        self.dbhelper = DBHelper()
        self.dbhelper.addPayment(self.roll, self.fee, self.semester)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rollToBeSearched = 0
        self.vbox = QVBoxLayout()
        self.text = QLabel("Numero da matricula: ")
        self.editField = QLineEdit()
        self.btnSearch = QPushButton("Pesquisar", self)
        self.btnSearch.clicked.connect(self.showStudent)
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.editField)
        self.vbox.addWidget(self.btnSearch)
        self.dialog = QDialog()
        self.dialog.setWindowTitle("NUMERO DE MATRICULA")
        self.dialog.setLayout(self.vbox)

        self.rollForPayment = 0
        self.vboxPayment = QVBoxLayout()
        self.textPayment = QLabel("MATRICULA NUMERO: ")
        self.editFieldPayment = QLineEdit()
        self.btnSearchPayment = QPushButton("Pesquisar", self)
        self.btnSearchPayment.clicked.connect(self.showStudentPayment)
        self.vboxPayment.addWidget(self.textPayment)
        self.vboxPayment.addWidget(self.editFieldPayment)
        self.vboxPayment.addWidget(self.btnSearchPayment)
        self.dialogPayment = QDialog()
        self.dialogPayment.setWindowTitle("NUMERO DE MATRICULA")
        self.dialogPayment.setLayout(self.vboxPayment)

        self.btnEnterStudent = QPushButton("Detalhes do estudante", self)
        self.btnEnterPayment = QPushButton("Detalhes do pagamento", self)
        self.btnShowStudentDetails = QPushButton("Mostrar detalhes do estudante", self)
        self.btnShowPaymentDetails = QPushButton("Mostrar detalhes do pagamento", self)

        self.picLabel = QLabel(self)
        self.picLabel.resize(150, 150)
        self.picLabel.move(180, 20)
        self.picLabel.setScaledContents(True)
        self.picLabel.setPixmap(QtGui.QPixmap("user.png"))

        self.btnEnterStudent.move(150, 170)
        self.btnEnterStudent.resize(240, 40)
        self.btnEnterStudentFont = self.btnEnterStudent.font()
        self.btnEnterStudentFont.setPointSize(13)
        self.btnEnterStudent.setFont(self.btnEnterStudentFont)
        self.btnEnterStudent.font.clicked.connect(self.enterstudent)

        self.btnEnterPayment.move(260, 170)
        self.btnEnterPayment.resize(240, 40)
        self.btnEnterPaymentFont = self.btnEnterStudent.font()
        self.btnEnterPaymentFont.setPointSize(13)
        self.btnEnterPayment.setFont(self.btnEnterPaymentFont)
        self.btnEnterPayment.font.clicked.connect(self.enterpayment)

        self.btnShowStudentDetails.move(15, 220)
        self.btnShowStudentDetails.resize(240, 40)
        self.btnShowStudentDetailsFont = self.btnShowStudentDetails.font()
        self.btnShowStudentDetailsFont.setPointSize(13)
        self.btnShowStudentDetails.setFont(self.btnShowStudentDetailsFont)
        self.btnShowStudentDetails.font.clicked.connect(self.showStudentDialog)

        self.btnShowPaymentDetails.move(260, 220)
        self.btnShowPaymentDetails.resize(240, 40)
        self.btnShowPaymentDetailsFont = self.btnShowPaymentDetails.font()
        self.btnShowPaymentDetailsFont.setPointSize(13)
        self.btnShowPaymentDetails.setFont(self.btnShowPaymentDetailsFont)
        self.btnShowPaymentDetails.font.clicked.connect(self.showStudentPaymentDialog)

        self.risize(520, 280)
        self.setWindowTitle("SISTEMA ESCOLAR === stu_dados")

    def enterstudent(self):
        enterStudent = AddStudent()

    def enterpayment(self):
        enterpayment = AddPayment()

    def showStudentDialog(self):
        self.dialog.exec()

    def showStudentPaymentDialog(self):
        self.dialogPayment.exec()

    def showStudent(self):
        if self.editField.text() is "":
            QMessageBox.warning(QMessageBox(), 'stu_dados', 'Digite o número da matricula para buscar')
            return None
        showstudent = DBHelper()
        showstudent.searchStudent(int(self.editField.text()))

    def showStudentPayment(self):
        if self.editField.text() is "":
            QMessageBox.warning(QMessageBox(), 'stu_dados', 'Digite o número da matricula para buscar')
            return None
        showstudent = DBHelper()
        showstudent.searchPayment(int(self.editFieldPayment.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()

    if login.exec_() == QDialog.Accepted:
        window = Window()
        window.show()
    sys.exit(app.exec_())
