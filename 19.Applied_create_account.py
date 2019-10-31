import sys
from PyQt5.QtWidgets import *                                                       # uygulama dosyamiz icin importlari yapalim
from design_create_account import *                                                 # designer uzerinden olusturulan dosyamizi buraya import ediyoruz
from PyQt5.QtWidgets import QMessageBox
import sqlite3 as sql


# ************************************** UYGULAMA *************************************************

class myApp(QtWidgets.QMainWindow):  # ilk olarak klass olusturup inheritance yapmaliyim
    def __init__(self):
        super(myApp, self).__init__()  # inheritance

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                                                       # designer dosyasindaki ilk def imizi cagiriyoruz

        self.ui.createaccountpushButton.clicked.connect(self.Create)                # simdi create butonumuzu cagiriyoruz bunun icin asagida def olusturacagiz
        self.ui.cancelpushButton.clicked.connect(self.Cancel)                       # cancel butonu cagiricisi
        self.ui.maleradioButton.toggled.connect(self.Gender)                        # male radiobutton kutucugu cagiricisi
        self.ui.femaleradioButton.toggled.connect(self.Gender)                      # female radiobutton kutucugu cagiricisi
        self.ui.readandacceptcheckBox.stateChanged.connect(self.Check_State)        # okudum kabul ediyorum cbox
        self.ui.marriedradioButton.toggled.connect(self.Marriage)                   # evli radiobuton cagiricisi
        self.ui.singleradioButton.toggled.connect(self.Marriage)                    # bekar radiobuton cagiricisi
        self.ui.actionClear.triggered.connect(self.ClearItems)                      # burasi File altinda ve girilen butun veriyi temizliyor
        self.ui.action_Ctrl_Q.triggered.connect(self.Cancel)                        # burasi File altinda ve direk cikis yapiyor
        self.ui.cancelpushButton.clicked.connect(self.ShowDialog1)                  # cancel butona tiklayinca verilen mesaj icin
        self.ui.actionZoom_In_Ctrl_1.triggered.connect(self.Zoom)                   # zoom in butona tiklayinca verilen mesaj icin
        self.ui.actionZoom_Out_Ctrl_0.triggered.connect(self.Zoom)                  # zoom out butona tiklayinca verilen mesaj icin
        self.ui.actionAbout.triggered.connect(self.ShowDialog4)                     # about butona tiklayinca verilen mesaj icin
        self.ui.actionInfo.triggered.connect(self.ShowDialog5)                      # info butona tiklayinca verilen mesaj icin

        self.ui.passwoordline.setEchoMode(2)                                        # Sifreyi gorunmez yapmak icin mod
        self.ui.conformpassline.setEchoMode(2)

    def Create(self):                                                               # Create diye yukardaki butonun def ini olusturduk
        if self.ui.readandacceptcheckBox.isChecked():                               # eger okudum ve kabul ediyorum isaretlerseniz hesap olusturulacak kontrolu

            self.username = self.ui.usernameline.text()                             # tasarim modundaki girilmesi gereken yerlere degisken atiyoruz
            self.name = self.ui.nameline.text()
            self.surname = self.ui.surnameline.text()
            self.genderr = self.Gender()
            self.marriage = self.Marriage()
            self.mail = self.ui.emailline.text()
            self.mail_again = self.ui.confirmemailline.text()
            self.password = self.ui.passwoordline.text()
            self.password_again = self.ui.conformpassline.text()

#***************Burasi mail ve sifrelerin uyusmama durumu icin dongu**********************************
            if self.mail != self.mail_again and self.password != self.password_again:
                QMessageBox.question(self, "Attention!", "Mail address and Password are conflict! Please correct them.", QMessageBox.Ok, QMessageBox.Ok)
            elif self.password != self.password_again:
                QMessageBox.question(self, "Attention!", "Password is conflict!! Please correct them.", QMessageBox.Ok, QMessageBox.Ok)
            elif self.mail != self.mail_again:
                QMessageBox.question(self, "Attention!", "Mail address is conflict! Please correct them.", QMessageBox.Ok, QMessageBox.Ok)
#***************Eger butun sartlar calisiyorsa sql kayit yapma yeri************************************
            else:
                self.connect_sql()                                                                                      # sql baglantimizi cagiriyoruz
                self.cursor.execute("""Select e_mail From Registration Where e_mail = ?""", (self.mail,))               # mail kontrol yeri database deki ile aynimi degilmi
                compare_mail = self.cursor.fetchall()
                if len(compare_mail) == 0:                                                                              # eger girilenin aynisi mail yoksa kayit yapsin
                    db = sql.connect("applied_create_account.db")
                    self.cursor = db.cursor()
                    self.cursor.execute("""INSERT INTO Registration ( username, name, surname, gender, marriage, e_mail, confirm_e_mail, password, confirm_password) 
                                                    values (?,?,?,?,?,?,?,?,?)""",
                                        (self.username, self.name, self.surname, self.genderr, self.marriage, self.mail,
                                         self.mail_again, self.password, self.password_again), )
                    crtmsg = QMessageBox.question(self, "Attention!", "Your Account Created SUCCESSFULLY...", QMessageBox.Ok, QMessageBox.Ok)
                    db.commit()
                    db.close()
                    if crtmsg == QMessageBox.Ok:                                                                       # eger kayittan sonra bir kayit daha yapmak istiyormusun soru kutusu
                        newmsg = QMessageBox.question(self, "Attention!", "Do you want to new account?",
                                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        if newmsg == QMessageBox.Yes:                                                                  # yes diyosan temizliyor
                            self.ClearItems()
                        else:                                                                                          # no diyosan cikiyor
                            QtWidgets.qApp.quit()
                else:                                                                                                  # bu mail kullaniliyor soru kutucugu
                    QMessageBox.question(self, "Close Application", "This e mail is using. Please, try another name...", QMessageBox.Ok, QMessageBox.Ok)

        else:                                                                                                          # eger okudum kabul ediom tiklanmadiysa mesaj versin!
            QMessageBox.question(self, "Control Check Box", "You have to read and click checkbox!", QMessageBox.Ok,
                                 QMessageBox.Ok)

    def ShowDialog1(self):                                                                                             # cancel denildiginde bize neler olacagini veren def fonksiyonu
        msg1 = QMessageBox.question(self, "Close Application", "Are you sure?",
                                    QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel, QMessageBox.Ok)          # aciklamalari asagida uzun sekilde verildi. Bu kisa kod versiyonudur.
        if msg1 == QMessageBox.Ok:
            QtWidgets.qApp.quit()

    # ********************** Uzun versiyonu asagidadir... *******************************************************************
    #     msg = QMessageBox()                                                     # tiklandiginda ne mesaji verecegimizi gosteren fonk
    #
    #     msg.setWindowTitle("Close Application")                                 # mesaj bix adini verir
    #     msg.setText("Are you sure?")                                            # ekrana nasil bir yazi gelmesini istiyorsak onu verir
    #     msg.setIcon(QMessageBox.Warning)                                        # ekrana uyari resmi veya butonu verir istersek degistirebiliriz
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)     # OK,ignore ve cancel diye 3buton yaptik arttirilabilir
    #     msg.setDefaultButton(QMessageBox.Cancel)                                # cancel butonu aktif olarak gorunme kodu hangisini istersek yapabiliriz
    #     msg.buttonClicked.connect(self.popup_button)                            # cikan yazilara islevsellik kazandirmak icin cagiriyoruz
    #     x = msg.exec_()                                                         # bu fonksiyonu calistirmak icin konulur
    #
    # def popup_button(self, i):
    #     if i == "Ok":                                                           # Ok secildiginde uygulamadan ciksin
    #         QtWidgets.qApp.quit()
    #     else:
    #         print("Let's Continue...")
    # ***********************************************************************************************************************

    def Zoom(self):                                                                                                     # zoom in out denildiginde bize neler olacagini veren def fonksiyonu
        chose = self.sender()
        self.ax = self.normalGeometry().getRect()[0]                                                                    # bunlar bizim grafigin normal boyutlaridir
        self.ay = self.normalGeometry().getRect()[1]
        self.aw = self.normalGeometry().getRect()[2]
        self.ah = self.normalGeometry().getRect()[3]
        if chose.text() == "Zoom In   (Ctrl+1)":
            self.setGeometry(self.ax, self.ay, self.aw + 50, self.ah + 50)
        elif chose.text() == "Zoom Out   (Ctrl+0)":
            self.setGeometry(self.ax, self.ay, self.aw - 50, self.ah - 50)

    def ShowDialog4(self):                                                                                              # about denildiginde bize neler olacagini veren def fonksiyonu
        msg4 = QMessageBox.question(self, "About", "What about you?",
                                    QMessageBox.YesAll | QMessageBox.No | QMessageBox.Reset, QMessageBox.YesAll)        # aciklamalari asagida uzun sekilde verildi. Bu kisa kod versiyonudur.
        if msg4 == QMessageBox.YesAll:
            Menu()

    def ShowDialog5(self):                                                                                              # info denildiginde bize neler olacagini veren def fonksiyonu
        msg5 = QMessageBox.question(self, "Info", "If you want to info then you can search from Internet :)",
                                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Retry,
                                    QMessageBox.Yes)                                                                    # aciklamalari asagida uzun sekilde verildi. Bu kisa kod versiyonudur.
        if msg5 == QMessageBox.Yes:
            Menu()

    def Check_State(self):                                                                                              # checkbox icin fonksiyon
        cb = self.sender()                                                                                              # sender bize male ve female cbox lari alir
        # print(cb.text())                                                                                              # secilen cbox in textini ekrana yazdirir

    def Marriage(self):                                                                                                 # *************marriage radiobutton**************
        # rb = self.sender()
        # print(rb.text())
        items2 = self.ui.centralwidget.findChildren(
            QRadioButton)                                                                                               # butun widgets lari items adinda degiskene tanimladik
        # result2 = ''                                                                                                  # bos bir string tanimlayip
        for rb in items2:
            if rb.isChecked():                                                                                          # cbox isaretlenenleri kontrol et
                return rb.text()
                # result2 += rb.text() + '\n'                                                                           # tiklananlar result a atsin her attiginda asagi insin
        # self.ui.marriageLabel.setText(result2)                                                                        # bizim sadece okudum isaretledimden farkli gender label cbox imiz mevcut. Dolayisiyla oraya eklesin. Eger farkli gruplar olsaydi herbiri icin farkli grup olusturup farkli def ve for dongusu yapip oraya eklememiz gerekiyordu
        # print(self.ui.marriageLabel)

    def Gender(self):                                                                                                   # ************gender radiobutton***************
        # rb = self.sender()
        # print(rb.text())
        items1 = self.ui.centralwidget.findChildren(
            QRadioButton)                                                                                               # butun widgets lari items adinda degiskene tanimladik
        # result1 = ''                                                                                                  # bos bir string tanimlayip
        for cb in items1:
            if cb.isChecked():                                                                                          # cbox isaretlenenleri kontrol et
                return cb.text()
                # result1 += cb.text() + '\n'                                                                           # check edilenleri result a atsin her attiginda asagi insin
        # self.ui.genderLabel.setText(result1)                                                                          # bizim sadece okudum isaretledimden farkli gender label cbox imiz mevcut. Dolayisiyla oraya eklesin. Eger farkli gruplar olsaydi herbiri icin farkli grup olusturup farkli def ve for dongusu yapip oraya eklememiz gerekiyordu
        # print(self.ui.genderLabel)

    def ClearItems(self):                                                                                               # file altindaki clear butonu def cagirmasi
#**************************** teker teker butun yerleri temizletiyoruz**************************
        self.ui.usernameline.clear()
        self.ui.nameline.clear()
        self.ui.surnameline.clear()
        self.ui.emailline.clear()
        self.ui.confirmemailline.clear()
        self.ui.passwoordline.clear()
        self.ui.conformpassline.clear()
        self.ui.readandacceptcheckBox.setChecked(False)
        # self.ui.genderr.setChecked(False)
        # self.ui.marriage.setChecked(False)

    def Cancel(self):                                                                                                   # Cancel diye yukardaki butonun def ini olusturduk
        Menu().quit()

    def connect_sql(self):                                                                                              # sql baglanti kurma fonksiyonu
        db = sql.connect("applied_create_account.db")
        self.cursor = db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Registration (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                                                username TEXT,
                                                                name TEXT NOT NULL,
                                                                surname TEXT NOT NULL,
                                                                gender TEXT,
                                                                marriage TEXT,
                                                                e_mail TEXT NOT NULL,
                                                                confirm_e_mail TEXT NOT NULL,
                                                                password TEXT NOT NULL,
                                                                confirm_Password TEXT NOT NULL)""")
        db.commit()


def Menu():
    app = QtWidgets.QApplication(sys.argv)                                                                              # dosyamizi calistirmak icin gerekli modul
    win = myApp()
    win.show()
    win.setWindowTitle("User Create Window")
    win.connect_sql()
    sys.exit(app.exec_())


Menu()
