from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import sys

class Ui_yardim(object):
    def setupUi(self, yardim):
        yardim.resize(400, 300)
        self.textBrowser = QTextBrowser(yardim)
        self.textBrowser.setGeometry(QRect(10, 20, 371, 261))
        yardim.setWindowTitle("Uygulama Info")
        info = "Bu kayit arayuzu 19.hafta pyqt ve sqlite uygulamalarinin kordine kullanilabilmesi odevidir."
        self.textBrowser.setText(info)

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget=MyWidget()
        self.setCentralWidget(self.widget)
        self.setWindowTitle("Kisisel Bilgiler")
        self.genislik=500
        self.yukseklik=500
        self.setGeometry(200,100,self.genislik,self.yukseklik)
        self.setUI()


    def setUI(self):
        self.menu=self.menuBar()
        self.file=self.menu.addMenu("Dosya")
        self.register=self.file.addAction("Kayit Ol")
        self.register.setShortcut("Ctrl+R")
        self.cancel=self.file.addAction("Iptal")
        self.cancel.setShortcut("Ctrl+I")
        self.exit=self.file.addAction("Cikis")
        self.exit.setShortcut("Ctrl+Q")


        self.view=self.menu.addMenu("Gorunum")
        self.zoom_in=self.view.addAction('Yakinlastir')
        self.zoom_out=self.view.addAction("Uzaklastir")

        self.help=self.menu.addMenu("Yardim")
        self.about=self.help.addMenu("Hakkinda")
        self.app_info=self.about.addAction("Uygulama Info")
        self.app_info.setShortcut('Ctrl+U')

        self.file.triggered[QAction].connect(self.file_func)
        self.view.triggered[QAction].connect(self.view_func)
        self.about.triggered[QAction].connect(self.help_func)




    def file_func(self,q):
        if q==self.register:
            self.widget.pushbutton_ok.click()
        elif q==self.cancel:
            self.widget.pushbutton_clear.click()
        elif q==self.exit:
            self.close()

    def view_func(self,q):
        if q==self.zoom_out:
            self.genislik-=50
            self.yukseklik-=50
            self.setGeometry(200,100,self.genislik,self.yukseklik)
        elif q==self.zoom_in:
            self.genislik += 50
            self.yukseklik += 50
            self.setGeometry(200,100, self.genislik, self.yukseklik)
    def help_func(self,q):
        if q==self.app_info:
            import sys
            self.app = QApplication([])
            self.yardim = QWidget()
            self.ui = Ui_yardim()
            self.ui.setupUi(self.yardim)
            self.yardim.show()
            self.app.exec_()



class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons()

    def buttons(self):
        self.mainbox_layout=QFormLayout()

        self.label_name=QLabel("Isim :")
        self.lineedit_name=QLineEdit()

        self.label_surname=QLabel("Soyadi :")
        self.lineedit_surname=QLineEdit()

        self.label_gender=QLabel("Cinsiyet :")
        self.radiobutton_female=QRadioButton("Kadin")
        self.radiobutton_male=QRadioButton("Erkek")
        self.group_gender=QButtonGroup()
        self.group_gender.addButton(self.radiobutton_female)
        self.group_gender.addButton(self.radiobutton_male)
        self.layout_gender = QHBoxLayout()
        self.layout_gender.addWidget(self.radiobutton_female)
        self.layout_gender.addWidget(self.radiobutton_male)

        self.label_maritalstation=QLabel("Medeni Durum :")
        self.radiobutton_maried=QRadioButton("Evli")
        self.radiobutton_single=QRadioButton("Bekar")
        self.group_marital=QButtonGroup()
        self.group_marital.addButton(self.radiobutton_maried)
        self.group_marital.addButton((self.radiobutton_single))
        self.layout_marital=QHBoxLayout()
        self.layout_marital.addWidget(self.radiobutton_maried)
        self.layout_marital.addWidget(self.radiobutton_single)

        self.label_graduation=QLabel("Mezuniyet:")
        self.combobox_graduation=QComboBox()
        self.combobox_graduation.addItems(["Lise","Lisans","Yuksek Lisans","Doktora"])


        self.label_mail=QLabel("E-Mail :")
        self.lineedit_mail=QLineEdit()
        self.label_mailrepeat=QLabel("Mail Tekrar:")
        self.lineedit_mailrepeat=QLineEdit()
        self.label_password=QLabel("Sifre :")
        self.lineedit_password=QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.label_passwordrepeat = QLabel("Sifre Tekrar :")
        self.lineedit_passwordrepeat = QLineEdit()
        self.lineedit_passwordrepeat.setEchoMode(QLineEdit.Password)

        self.label_contrat=QLabel("Sozlesme Sartlari:")
        self.text_contrat=QTextEdit()

        self.checkbutton=QCheckBox("Sozlesmeyi okudum,kabul ediyorum.")
        self.durumline=QLineEdit()
        self.durumline.setReadOnly(True)
        self.durumline.setText("")

        self.pushbutton_ok=QPushButton("Kayit Ol")
        self.pushbutton_clear=QPushButton("Temizle")
        self.end_layout = QHBoxLayout()
        self.end_layout.addStretch()
        self.end_layout.addWidget(self.pushbutton_ok)
        self.end_layout.addStretch()
        self.end_layout.addWidget(self.pushbutton_clear)
        self.end_layout.addStretch()

        self.mainbox_layout.addRow(self.label_name,self.lineedit_name)
        self.mainbox_layout.addRow(self.label_surname,self.lineedit_surname)
        self.mainbox_layout.addRow(self.label_gender,self.layout_gender)
        self.mainbox_layout.addRow(self.label_maritalstation,self.layout_marital)
        self.mainbox_layout.addRow(self.label_mail,self.lineedit_mail)
        self.mainbox_layout.addRow(self.label_mailrepeat,self.lineedit_mailrepeat)
        self.mainbox_layout.addRow(self.label_password,self.lineedit_password)
        self.mainbox_layout.addRow(self.label_passwordrepeat, self.lineedit_passwordrepeat)
        self.mainbox_layout.addRow(self.label_graduation,self.combobox_graduation)
        self.mainbox_layout.addRow(self.label_contrat,self.text_contrat)
        self.mainbox_layout.addRow(self.checkbutton)
        self.mainbox_layout.addRow(self.durumline)

        self.mainbox_layout.addItem(self.end_layout)
        self.setLayout(self.mainbox_layout)

        self.pushbutton_clear.clicked.connect(self.cleaar)
        self.pushbutton_ok.clicked.connect(self.kontrol)
    def cleaar(self):
        self.pushbutton_clear.clicked.connect(self.lineedit_passwordrepeat.clear)
        self.pushbutton_clear.clicked.connect(self.lineedit_password.clear)
        self.pushbutton_clear.clicked.connect(self.lineedit_mailrepeat.clear)
        self.pushbutton_clear.clicked.connect(self.lineedit_mail.clear)
        self.pushbutton_clear.clicked.connect(self.lineedit_surname.clear)
        self.pushbutton_clear.clicked.connect(self.lineedit_name.clear)
        self.pushbutton_clear.clicked.connect(self.durumline.clear)




    def kontrol(self):
        if self.checkbutton.isChecked()==False:
            self.durumline.setText("Sozlesmeyi kabul etmelisiniz")
        elif len(self.lineedit_name.text())==0 or len(self.lineedit_surname.text())==0 or len(self.lineedit_mail.text())==0 or len(self.lineedit_password.text())==0:
            self.durumline.setText("Isim,soyisim,e-mail ve sifre bolumleri bos birakilamaz!!")
        elif self.lineedit_mail.text()!= self.lineedit_mailrepeat.text():
            self.durumline.setText("Tekrar girilen mail adresi uyusmuyor!!")
        elif self.lineedit_password.text()!= self.lineedit_passwordrepeat.text():
            self.durumline.setText("Tekrar girilen sifre uyusmuyor!!")
        else:
            self.register()

    def register(self):

        name = self.lineedit_name.text()
        surname = self.lineedit_surname.text()
        gender = "Kadin" if self.radiobutton_female.isChecked() == True else "Erkek"
        marital = "Evli" if self.radiobutton_maried.isChecked() == True else "Bekar"
        graduation = self.combobox_graduation.currentText()
        mail = self.lineedit_mail.text()
        password = self.lineedit_password.text()

        vt = sqlite3.connect("database.db")
        self.cursor = vt.cursor()
        self.cursor.execute("Select * From kullanici Where mail = ?", (self.lineedit_mail.text(),))
        data = self.cursor.fetchall()
        if len(data)>0:
            self.durumline.setText("Bu mail adresi daha once kullanilmistir!!")
        else:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS kullanici (ad TEXT, soyad TEXT,cinsiyet TEXT, medenidurum TEXT,egitim TEXT, mail TEXT, sifre TEXT)")

        vt = sqlite3.connect("database.db")
        self.cursor = vt.cursor()
        self.cursor.execute("Insert into kullanici values (?,?,?,?,?,?)", (
            name, surname, gender, marital,graduation, mail, password,))
        vt.commit()
        vt.close()


    

app=QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec())

