from PyQt5.QtWidgets import *
from hafta19son import *
import sqlite3

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.ui.create_account.clicked.connect(self.Create)
        self.ui.menuFile.triggered.connect(self.File)
        self.ui.menuView.triggered.connect(self.View)
        self.ui.menuHelp.triggered.connect(self.Help)

    def Create(self):
        kayit = sqlite3.connect("database.db")
        self.cursor = kayit.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'kayit_defteri' ('isim' TEXT, 'soyisim' TEXT, 'email' TEXT, 
        'parola' TEXT)""")

        self.isim = str(self.ui.lineEdit.text())
        self.soyisim = str(self.ui.lineEdit_2.text())
        self.email = str(self.ui.lineEdit_3.text())
        self.parola = str(self.ui.lineEdit_5.text())

        self.cursor.execute("SELECT email From kayit_defteri where email = ?", (self.email,))
        bilgi = self.cursor.fetchall()

        if len(bilgi) == 0:
            self.cursor.execute("INSERT INTO kayit_defteri(isim,soyisim,email,parola) VALUES (?,?,?,?)",(self.isim, self.soyisim, self.email, self.parola))
            self.ui.uyarialani.setText("Congratulations. Your account has been created. \nYou can now access all of our facilities. Have a good time! ")
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_3.setChecked(False)
            self.ui.checkBox_4.setChecked(False)
            self.ui.checkBox_5.setChecked(False)
            self.ui.groupBox.setChecked(False)
        else:
            self.ui.uyarialani.setText("This email address is already exist.\nPlease try another address.")
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()

        kayit.commit()

    def File(self,action):
        if action.text() == "Cancel":
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_3.setChecked(False)
            self.ui.checkBox_4.setChecked(False)
            self.ui.checkBox_5.setChecked(False)
            self.ui.groupBox.setChecked(False)
            self.ui.uyarialani.clear()
        if action.text() == "Create Account":
            self.Create()
        elif action.text() == "Quit":
            quit()

    def View(self,action):
        if action.text() == "Zoom In":
            pencere.resize(700,700)
        elif action.text() == "Zoom Out":
            pencere.resize(1300,800)

    def Help(self,action):
        if action.text() == "Webpage Info":
            self.ui.uyarialani.setText("Daha fazla bilgi icin www.createaccount.com sitemizi ziyaret edebilirsiniz.")

uygulama = QApplication([])
pencere = Pencere()
pencere.setWindowTitle("CREATE A NEW ACCOUNT")
pencere.resize(1000,900)
pencere.show()
uygulama.exec_()
