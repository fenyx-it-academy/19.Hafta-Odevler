
from PyQt5.QtWidgets import *
from kayitui import *
import sqlite3
#***************database olusturma****************************
veri_tb=sqlite3.connect ("C:\\Users\\Gebruiker\\Desktop\\19.hafta2\\kayit_son.db")
imlec=veri_tb.cursor()

imlec.execute ( "DROP TABLE IF EXISTS Kayit" )
tablo_yap= """CREATE TABLE IF NOT EXISTS Kayit
(id integer PRIMARY KEY AUTOINCREMENT,ISIM text NOT NULL,SOYISIM text,
MEDENI_DURUMUNUZ TEXT,E_MAIL text,E_MAIL_TEKRAR TEXT,PASWORD TEXT,PASWORD_TEKRAR TEXT,CINSIYET TEXT )"""

imlec.execute(tablo_yap)
veri_tb.commit()
#*******************pencere Class************************************

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        # ui dosyasindan donusturulen kayit.py dosyasinin clasini cagiriyoruz
        self.ui=Ui_MainWindow()
        self.ui.setupUi ( self )

        self.ui.Evli.toggled.connect ( self.Med_hal )  # cinsiyet secme 'Evli' radio butonunu tiklanma durumu fonksiyonu
        self.ui.Bekar.toggled.connect ( self.Med_hal )  # cinsiyet secme 'Bekar' radio butonunu tiklanma durumu fonksiyonu

        self.ui.bayan.toggled.connect ( self.cins )#cinsiyet secme 'bayan' radio butonunu tiklanma durumu fonksiyonu
        self.ui.erkek.toggled.connect ( self.cins )#cinsiyet secme 'erkek' radio butonunu tiklanma durumu fonksiyonu

        self.ui.kontrol.stateChanged.connect ( self.kontrol_et ) #checkbox kutusunun durumunu gosteren fonksiyon
                                                               #bu fonksiyon bir de Value degeri doner
        self.ui.buton_kayit.clicked.connect( self.kaydet )#kaydet butonu durumunu gosteren fonksiyon
        self.ui.buton_esc.clicked.connect ( self.iptal_et )#iptal butonu fonksiyonu
        self.ui.Temizle.clicked.connect( self.secreen_clear ) #temizle butonu

        self.ui.Kayit_ol.triggered.connect( self.kaydet ) #dosya menusundeki Kaydet butonu
        self.ui.Iptal.triggered.connect( self.iptal_et )       #dosya menusundeki iptal butonu
        self.ui.Cikis.triggered.connect ( self.kapat )  #dosya menusundeki Cikis butonu

        self.ui.Yakinlastir.triggered.connect( self.focus_window )  #Gorunum menusundeki Yakinlastir butonu
        self.ui.Uzaklastir.triggered.connect( self.focus_window )#Gorunum menusundeki Uzaklastir butonu

    def focus_window(self):# Gorunum kisminda yaklasma ve uzaklasma fonksiyonu
        sec=self.sender()
        print(sec.text())
        if sec.text()=="Uzaklastir":
            self.setGeometry(400,100,200,100)
        elif sec.text()=="Yakinlastir":
            self.setGeometry(5,30,1400,700)

    def kapat(self):#kapatma fonksiyonu
        quit()

    def Med_hal(self): # radio butonlarinin fonksiyonu
        sender = self.sender ()
        if sender.isChecked () : #true degeri doner
            self.MEDENI_DURUM=sender.text() #True degerini yazdirma komutu
            return self.MEDENI_DURUM

    def cins(self): # radio butonlarinin fonksiyonu
        sender = self.sender ()
        if sender.isChecked () : #true degeri doner
            self.CINSIYET=sender.text() #True degerini yazdirma komutu
            return self.CINSIYET

    def kontrol_et(self,value): #checkbox kutusunun fonksiyonu Value degeri de dondurur
        self.kontrol_sagla=value
        return self.kontrol_sagla

    def kaydet(self): #penceredeki degerleri bu fonksiyonda tanimladik
        try:
            secim = self.sender ().text ()
            # print ( secim )
            ISIM = self.ui.ad_line.text ()
            SOYISIM = self.ui.soyad_line.text ()
            PASWORD = self.ui.pas_line.text ()
            PASWORD_TEKRAR = self.ui.pas_tek_line.text ()
            E_MAIL = self.ui.mail_line.text ()
            E_MAIL_TEKRAR = self.ui.mail_tekrar_line.text ()
            KAYDET_DOSYA=self.ui.Kayit_ol.text() # dosya menusundeki Kaydet butonu text degeri

            #*************************Email Ayni olma durumunu kontrol etme***************************************
            imlec.execute("select E_MAIL from Kayit where E_MAIL=?",(E_MAIL,)); #Email Ayni olma durumunu kontrol etme
            oku=imlec.fetchone()

            if oku!=None:
                print('Bu mail daha once kullanildi')
                self.ui.label.setText( "Bu e_mail kullanildi ,yeni e_mail giriniz..." )

            #************************************************************************************
            elif len(PASWORD)<8:
                self.ui.label.setText ( "Lutfen bilgilerin dogru girildiginden emin olun (Parolaniz en az 8 karakter olmalidir)" )

            #************Kaydetme  ve database kaydetme bolumu*************************************

            elif (secim=='KAYDET' or KAYDET_DOSYA=='Kaydet') and E_MAIL==E_MAIL_TEKRAR and PASWORD==PASWORD_TEKRAR and self.kontrol_sagla==2 :

                self.ui.label.setText( "Kayit tamamlandi lutfen yeni kayit icin TEMIZLE tusuna basiniz" )

                print('isim :'+ISIM,'soyisim :'+SOYISIM,'medeni durumu :'+self.MEDENI_DURUM,'email :'+E_MAIL,'email tekrar :'+E_MAIL_TEKRAR,
                      'pasword :'+PASWORD,'pasword tekrar :'+PASWORD_TEKRAR,'cinsiyet :'+self.CINSIYET,sep = '\n')

                deger = "INSERT INTO Kayit (ISIM ,SOYISIM,MEDENI_DURUMUNUZ,E_MAIL ,E_MAIL_TEKRAR,PASWORD,PASWORD_TEKRAR ,CINSIYET ) " \
                        "VALUES (?,?,?,?,?,?,?,?)"
                values=(ISIM,SOYISIM,self.MEDENI_DURUM,E_MAIL,E_MAIL_TEKRAR ,PASWORD,PASWORD_TEKRAR,self.CINSIYET )
                imlec.execute(deger,values);
                veri_tb.commit ()

                print("*******************************************************************************")


            else:
                print('lutfen hepsini doldurdugunuzdan emin olun')
                self.ui.label.setText ( "Lutfen bilgilerin dogru girildiginden emin olun" )

        except:
            print('lutfen tum seceneklere giris yapiniz')
            self.ui.label.setText ( "Lutfen bilgilerin dogru girildiginden emin olun" )
    #***************Ekrani temizleme fonksiyonlari***********************************
    def iptal_et(self):
        self.secreen_clear()

    def secreen_clear(self) :
        self.ui.label.clear ()
        self.ui.ad_line.clear ()
        self.ui.soyad_line.clear ()
        self.ui.mail_line.clear ()
        self.ui.mail_tekrar_line.clear ()
        self.ui.pas_line.clear ()
        self.ui.pas_tek_line.clear ()
        self.ui.kontrol.setChecked ( False )
        self.ui.bayan.setChecked ( False )
        self.ui.erkek.setChecked ( False )
        self.ui.Evli.setChecked ( False )
        self.ui.Bekar.setChecked ( False )


def Ana_Menu():
    App=QApplication([])
    win=MyApp()
    win.show()
    App.exec()

Ana_Menu()
veri_tb.close()






