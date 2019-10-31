from PyQt5.QtWidgets import *
from User_Registration_Form import *
import sqlite3 as sql
import os

# Connecting to DB
con = sql.connect("database.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS 'users' ('fName' TEXT, 'lName' TEXT, 'email' TEXT, 
                'password' TEXT, 'cellPhone' TEXT)""")
con.commit()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # ############ Sign Up Button Event ######################
        self.ui.singUp_button.clicked.connect(self.signUp_btn_event)
        # ########################################################

        # ############ Cancel Button Event ######################
        self.ui.cancel_button.clicked.connect(self.cancel_btn_event)
        # ########################################################

        # ############  Menu Events ###############################
        self.ui.menuFile.triggered.connect(self.File)
        self.ui.menuView.triggered.connect(self.View)
        self.ui.menuHelp.triggered.connect(self.Help)
        # ########################################################

    def signUp_btn_event(self):
        self.fName = str(self.ui.firstName_lineEdit.text()).title()
        self.ui.firstName_label.setStyleSheet("color: #33423B")
        self.lName = str(self.ui.lastName_lineEdit.text()).title()
        self.ui.lastName_label.setStyleSheet("color: #33423B")
        self.password = str(self.ui.password_lineEdit.text())
        self.ui.password_label.setStyleSheet("color: #33423B")
        self.ui.rePassword_label.setStyleSheet("color: #33423B")
        self.email = str(self.ui.email_lineEdit.text())
        self.ui.email_label.setStyleSheet("color: #33423B")
        self.ui.reEmail_label.setStyleSheet("color: #33423B")
        self.cellPhone = str(self.ui.cellPhone_lineEdit.text())
        cur.execute("SELECT email From users where email = ?", (self.email,))
        self.email_valid = cur.fetchall()

        if len(self.fName) != 0:
            if len(self.lName) != 0:
                if len(self.password) != 0:
                    if len(self.ui.rePassword_lineEdit.text()) != 0 and \
                            self.ui.rePassword_lineEdit.text() == self.password :
                        if len(self.email) != 0:
                            if len(self.ui.reEmail_lineEdit.text()) != 0 and \
                                    self.ui.reEmail_lineEdit.text() == self.email:
                                if len(self.email_valid) == 0:
                                    if self.ui.i_agree_checkBox.isChecked():
                                        cur.execute("INSERT INTO users(fName,lName,email,password,cellPhone) VALUES (?,?,?,?,?)",
                                                            (self.fName, self.lName, self.email, self.password, self.cellPhone))
                                        con.commit()
                                        self.ui.button_click_text_area.setText(
                                            "Congratulations. Your account has been created!")
                                        self.ui.firstName_lineEdit.clear()
                                        self.ui.lastName_lineEdit.clear()
                                        self.ui.password_lineEdit.clear()
                                        self.ui.rePassword_lineEdit.clear()
                                        self.ui.email_lineEdit.clear()
                                        self.ui.reEmail_lineEdit.clear()
                                        self.ui.cellPhone_lineEdit.clear()
                                        self.ui.gen_male_radioButton.setChecked(False)
                                        self.ui.gen_female_radioButton.setChecked(False)
                                        self.ui.gen_prefNotToSay_radioButton.setChecked(False)
                                        self.ui.ms_married_radioButton.setChecked(False)
                                        self.ui.ms_single_radioButton.setChecked(False)
                                        self.ui.ms_prefNotToSay_radioButton.setChecked(False)
                                        self.ui.i_agree_checkBox.setChecked(False)
                                    else:
                                        self.ui.button_click_text_area.setText("You must agree to the terms to sign up!")
                                else:
                                    self.ui.email_label.setStyleSheet("color: #FF0000")
                                    self.ui.button_click_text_area.setText("This email address already exists."
                                                                           "\nPlease enter another address.")
                            else:
                                self.ui.reEmail_label.setStyleSheet("color: #FF0000")
                                self.ui.button_click_text_area.setText("Email address doesn't match!")
                        else:
                            self.ui.email_label.setStyleSheet("color: #FF0000")
                            self.ui.button_click_text_area.setText("Email field cannot be blank!")
                    else:
                        self.ui.rePassword_label.setStyleSheet("color: #FF0000")
                        self.ui.button_click_text_area.setText("Password doesn't match!")
                else:
                    self.ui.password_label.setStyleSheet("color: #FF0000")
                    self.ui.button_click_text_area.setText("Password field cannot be blank!")
            else:
                self.ui.lastName_label.setStyleSheet("color: #FF0000")
                self.ui.button_click_text_area.setText("Last Name field cannot be blank!")
        else:
            self.ui.firstName_label.setStyleSheet("color: #FF0000")
            self.ui.button_click_text_area.setText("First name field cannot be blank!")

    def cancel_btn_event(self):
        self.ui.button_click_text_area.setText("You canceled your registration!")
        self.ui.firstName_lineEdit.clear()
        self.ui.lastName_lineEdit.clear()
        self.ui.password_lineEdit.clear()
        self.ui.rePassword_lineEdit.clear()
        self.ui.email_lineEdit.clear()
        self.ui.reEmail_lineEdit.clear()
        self.ui.cellPhone_lineEdit.clear()
        self.ui.gen_male_radioButton.setChecked(False)
        self.ui.gen_female_radioButton.setChecked(False)
        self.ui.gen_prefNotToSay_radioButton.setChecked(False)
        self.ui.ms_married_radioButton.setChecked(False)
        self.ui.ms_single_radioButton.setChecked(False)
        self.ui.ms_prefNotToSay_radioButton.setChecked(False)
        self.ui.i_agree_checkBox.setChecked(False)
        ###
        self.ui.firstName_label.setStyleSheet("color: #33423B")
        self.ui.lastName_label.setStyleSheet("color: #33423B")
        self.ui.password_label.setStyleSheet("color: #33423B")
        self.ui.rePassword_label.setStyleSheet("color: #33423B")
        self.ui.email_label.setStyleSheet("color: #33423B")
        self.ui.reEmail_label.setStyleSheet("color: #33423B")

    def File(self, action):
        if action.text() == "Sign Up":
            self.signUp_btn_event()
        elif action.text() == "Cancel":
            self.cancel_btn_event()
        elif action.text() == " Quit ":
            qApp.quit()

    def View(self, action):
        if action.text() == "Zoom In":
            win.resize(850, 850)
        elif action.text() == "Zoom Out":
            win.resize(650, 650)

    def Help(self, action):
        if action.text() == "Info":
            self.ui.button_click_text_area.setText("\t  Designed by H.Tunctepe as a PyCoders project." +
                                                   "\n\tFor more information visit http://www.pycoders.nl")

app = QApplication([])
win = MyWindow()
win.setWindowTitle("USER REGISTRATION FORM")
win.resize(750, 750)
win.show()
app.exec()
