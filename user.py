import sqlite3 as sql
from PyQt5.QtWidgets import *
from deneme1 import Ui_MainWindow
from PyQt5.QtCore import *


################# CREATE DATABASE and TABLE #############################

data = sql.connect(".\\user_database.db")
cursor = data.cursor()

create_user_table = """CREATE TABLE IF NOT EXISTS Registration ( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                                                isim TEXT,
                                                                soyisim TEXT,
                                                                cinsiyet TEXT,
                                                                medeni_durum TEXT,
                                                                mail TEXT,
                                                                mail_tekrar TEXT,
                                                                password TEXT,
                                                                password_tekrar TEXT,
                                                                onay TEXT
                                                                )"""

cursor.execute(create_user_table)
data.commit()
######################## APPLICATION #######################################


class Kayit(QMainWindow):
    def __init__(self):
        super(Kayit,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.On_disable()

        self.ui.btn_ok.clicked.connect(self.Kaydet)
        self.ui.btn_yeni_kayit.clicked.connect(self.Off_Disable)
        self.ui.btn_cancel.clicked.connect(self.close)

        self.ui.act_yeni_kayit.triggered.connect(self.Off_Disable)
        self.ui.act_kaydet.triggered.connect(self.Kaydet)
        self.ui.act_cikis.triggered.connect(self.close)
        self.ui.act_yakinlastir.triggered.connect(self.Zoom)
        self.ui.act_uzaklastir.triggered.connect(self.Zoom)

        self.ui.lne_password.setEchoMode(2)       ### SIFREYI GORUNMEZ YAPMA
        self.ui.lne_Password_again.setEchoMode(2) ### SIFREYI GORUNMEZ YAPMA

    def Zoom(self):
        secim = self.sender()
        self.ax = self.normalGeometry().getRect()[0]
        self.ay = self.normalGeometry().getRect()[1]
        self.aw = self.normalGeometry().getRect()[2]
        self.ah = self.normalGeometry().getRect()[3]
        if secim.text()=="Yakinlastir":
            self.setGeometry(self.ax, self.ay, self.aw+50, self.ah+50)
        elif secim.text()=="Uzaklastir" :
            self.setGeometry(self.ax,self.ay, self.aw-50, self.ah-50)


########### FORM DA GIRIS YAPILACAK YERLERI PASIF YAPIYOR #########
    def On_disable(self):
        self.disable_list = [self.ui.lne_ad, self.ui.lne_soyad,self.ui.lne_mail,self.ui.lne_mail_again,self.ui.lne_password,self.ui.lne_Password_again, self.ui.lbl_kayit_mesaj,
                        self.ui.rdb_erkek,self.ui.rdb_kadin, self.ui.chb_uyelik_onay,self.ui.cmb_med_durum,self.ui.btn_ok, self.ui.btn_cancel]


        for items in self.disable_list: items.setEnabled(False)
        self.ui.btn_yeni_kayit.setEnabled(True)


########## FORM DA GIRIS YAPILACAK YERLERI AKTIF YAPIYOR #######
    def Off_Disable(self):

        for indx in range(len(self.disable_list)):
            self.disable_list[indx].setEnabled(True)
            if indx<7:
                self.disable_list[indx].clear()
            elif 7<=indx<=9:
                self.disable_list[indx].setChecked(False)

        self.ui.btn_yeni_kayit.setEnabled(False)
        self.ui.cmb_med_durum.setCurrentIndex(0)


    def Cinsiyet_Kontrol(self):
        items = self.ui.frame_cinsiyet.findChildren(QRadioButton)
        for rb in items:
            if rb.isChecked():
                return rb.text()


############ HATA ALANLARINDA MESAJ OLUP OLMADIGINI KONTROL EDEN FONKSIYON #############################
    def ErrorCheckd(self):
        items = self.ui.ErrorMessageBox.findChildren(QLabel)
        for lbl in items:
            if lbl.text():
                return True
        if self.ui.lbl_onay_check.text():
            return True
        return False


############ DOLDURULMASI GREKIPTE BOS BIRAKILAN ALANLARIN KONTROLUNU YAPIP HATA MESAJI VERIYOR #########

    def PrintErrorMesages(self):
        self.liste1 = [self.name, self.mail, self.mail_again, self.password, self.password_again, self.onay]
        self.liste2 = self.ui.ErrorMessageBox.findChildren(QLabel)
        self.liste2 +=[self.ui.lbl_onay_check]

        for indx in range(len(self.liste1)):
            self.liste2[indx].clear()
            if not self.liste1[indx]:   ##### BOS ALANLAR ICIN UYARI MESAJI GOSTERILMESI
                self.liste2[indx].setText("lutfen bu alani bos birakmayiniz")

            if indx == 1 and not self.liste2[1].text():  ##### MAIL DATABASE ILE KARSILASTIRILIP UYARI MESAJI VERILMESI
                cursor.execute(""" SELECT mail FROM Registration WHERE mail=? """, (self.mail,))
                mail_karsilastirma = cursor.fetchone()
                if mail_karsilastirma:
                    self.liste2[indx].setText("Bu e-mail adresi kullanilmaktadir. Lutfen yeni bir e-mail giriniz")

            if indx == 2 and not self.liste2[2].text(): ##### MAIL ILK YAZILAN MAIL ADRESI ILE DOGRULAMA YAPMA
                if self.mail != self.mail_again:
                    self.liste2[indx].setText("Lutfen mail adresini tekrar kontrol ediniz...")

            if indx == 4 and not self.liste2[4].text(): ##### TEKRAR YAZILAN SIFRENIN DOGRULUGUNU KONTROL ETME.
                if self.password != self.password_again:
                    self.liste2[indx].setText("Lutfen Sifrenizi tekrar kontrol ediniz...")

    def Kaydet(self):
        self.name = self.ui.lne_ad.text()
        self.surname = self.ui.lne_soyad.text()
        self.gender = self.Cinsiyet_Kontrol()
        self.status = self.ui.cmb_med_durum.currentText()
        self.mail = self.ui.lne_mail.text()
        self.mail_again = self.ui.lne_mail_again.text()
        self.password = self.ui.lne_password.text()
        self.password_again  = self.ui.lne_Password_again.text()
        self.onay = self.ui.chb_uyelik_onay.isChecked()

        self.PrintErrorMesages()

        if not self.ErrorCheckd():
            cursor.execute("""INSERT INTO Registration ( isim,soyisim,cinsiyet, medeni_durum, mail, mail_tekrar, password, password_tekrar, onay ) 
            values (?,?,?,?,?,?,?,?,?)""",(self.name,self.surname,self.gender,self.status,self.mail,self.mail_again,self.password,self.password_again,self.onay))
            data.commit()
            self.ui.lbl_kayit_mesaj.setText("******** KAYDINIZ BASARI ILE YAPILDI *******")
            self.On_disable()

    def Cikis(self):
        pass

app = QApplication([])
pencere = Kayit()
pencere.show()
app.exec()

