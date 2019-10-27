import os
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from Odev import *

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.setWindowTitle("Kayit Ol")
        self.yazi_alani = QtWidgets.QLabel("")

        self.ui.pushButton_2.clicked.connect(self.Kaydet)
        self.ui.pushButton.clicked.connect(self.Iptal)




        self.menuleri_olustur()
        self.baglanti_olustur()

    def Iptal(self):
        pencere.close()

    def Kaydet(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "database.db", os.getenv(""))

        with open(dosya_ismi[0], "a+") as file:
            file.write(self.yazi_alani.toPlainText())




    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If not exists uyeler(ADi TEXT,Mail TEXT)")

        baglanti.commit()

        self.ui.pushButton_2.clicked.connect(self.login)

    def login(self):
        adi = self.ui.label.text()
        mail = self.ui.label_5.text()

        self.cursor.execute("select * from uyeler where Mail = ? (mail)")

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("boyle bir mail yok")
        elif len(data):
            if data == "emrlglcn@gmail.com":
                self.yazi_alani.setText("bu mail baska bir kullaniciya ait")
            else:
                self.data.Kaydet()


    def menuleri_olustur(self):
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")

        dosya_ac =QAction("ac",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        dosya_iptal = QAction("iptal",self)
        dosya_iptal.setShortcut("Ctrl+Q")

        dosya_temizle = QAction("temzile",self)
        dosya_temizle.setShortcut("Ctrl+R")

        cikis = QAction("cikis",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(dosya_iptal)
        dosya.addAction(dosya_temizle)
        dosya.addAction(cikis)

        gorunum = menubar.addMenu("Gorunum")

        gorunum_yakinlastir = QAction("Yakinlastir",self)
        gorunum_yakinlastir.setShortcut("Ctrl+Y")

        gorunum_uzaklastir = QAction("Uzaklastir",self)
        gorunum_uzaklastir.setShortcut("Ctrl+U")

        gorunum.addAction(gorunum_yakinlastir)
        gorunum.addAction(gorunum_uzaklastir)

        yardim = menubar.addMenu("Yardim")
        gorunum_hakkinda = QAction("Hakkinda",self)

        yardim.addAction(gorunum_hakkinda)

        dosya.triggered.connect(self.Basildi)



        self.show()

    def Basildi(self,action):
        if action.text() == "ac":
            dosya_ismi=QFileDialog.getOpenFileName(self,"database.db",os.getenv(""))

            with open(dosya_ismi[0],"r") as file:
                self.yazi_alani.setText(file.read())

        elif action.text() == "kaydet":
            self.pencere.Kaydet()

        elif action.text() == "iptal":
            self.pencere.Iptal()

        elif action.text() == "temizle":
            self.yazi_alani.clear()

        elif action.text() == "cikis":
            qApp.quit()








app = QApplication([])
pencere = Pencere()
pencere.show()
app.exec_()


