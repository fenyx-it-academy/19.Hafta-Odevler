# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_Registration_Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 729)
        MainWindow.setStyleSheet("background-color: rgb(213, 248, 232)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 20, 566, 611))
        self.widget.setObjectName("widget")
        self.main_vLayout = QtWidgets.QVBoxLayout(self.widget)
        self.main_vLayout.setContentsMargins(0, 0, 0, 0)
        self.main_vLayout.setObjectName("main_vLayout")
        self.uRegForm_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.uRegForm_label.setFont(font)
        self.uRegForm_label.setStyleSheet("color: #8E1F42")
        self.uRegForm_label.setObjectName("uRegForm_label")
        self.main_vLayout.addWidget(self.uRegForm_label)
        self.account_label = QtWidgets.QLabel(self.widget)

        font = QtGui.QFont()
        font.setPointSize(18)
        self.account_label.setFont(font)
        self.account_label.setStyleSheet("color: #B84C6F")
        self.account_label.setObjectName("account_label")
        self.main_vLayout.addWidget(self.account_label)
        self.firstName_hLayout = QtWidgets.QHBoxLayout()
        self.firstName_hLayout.setObjectName("firstName_hLayout")
        self.firstName_label = QtWidgets.QLabel(self.widget)
        self.firstName_label.setStyleSheet("color: #33423B")
        self.firstName_label.setObjectName("firstName_label")
        self.firstName_label.setFixedWidth(118)
        self.firstName_hLayout.addWidget(self.firstName_label)

        self.firstName_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.firstName_lineEdit.setStyleSheet("background-color: white")
        self.firstName_lineEdit.setObjectName("firstName_lineEdit")
        self.firstName_hLayout.addWidget(self.firstName_lineEdit)
        self.main_vLayout.addLayout(self.firstName_hLayout)


        self.lastName_hLayout = QtWidgets.QHBoxLayout()

        self.lastName_hLayout.setObjectName("lastName_hLayout")
        self.lastName_label = QtWidgets.QLabel(self.widget)
        self.lastName_label.setStyleSheet("color: #33423B")
        self.lastName_label.setObjectName("lastName_label")
        self.lastName_label.setFixedWidth(118)
        self.lastName_hLayout.addWidget(self.lastName_label)

        self.lastName_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lastName_lineEdit.setMinimumSize(QtCore.QSize(318, 0))
        self.lastName_lineEdit.setStyleSheet("background-color: white")
        self.lastName_lineEdit.setObjectName("lastName_lineEdit")
        self.lastName_hLayout.addWidget(self.lastName_lineEdit)
        self.main_vLayout.addLayout(self.lastName_hLayout)


        self.passwd_hLayout = QtWidgets.QHBoxLayout()

        self.passwd_hLayout.setObjectName("passwd_hLayout")
        self.password_label = QtWidgets.QLabel(self.widget)
        self.password_label.setStyleSheet("color: #33423B")
        self.password_label.setObjectName("password_label_10")
        self.password_label.setFixedWidth(118)
        self.passwd_hLayout.addWidget(self.password_label)

        self.password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(318, 0))
        self.password_lineEdit.setStyleSheet("background-color: white")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.passwd_hLayout.addWidget(self.password_lineEdit)
        self.main_vLayout.addLayout(self.passwd_hLayout)


        self.rePasswd_hLayout = QtWidgets.QHBoxLayout()
        self.rePasswd_hLayout.setObjectName("rePasswd_hLayout")

        self.rePassword_label = QtWidgets.QLabel(self.widget)
        self.rePassword_label.setStyleSheet("color: #33423B")
        self.rePassword_label.setObjectName("rePassword_label")
        self.rePassword_label.setFixedWidth(118)
        self.rePasswd_hLayout.addWidget(self.rePassword_label)

        self.rePassword_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.rePassword_lineEdit.setMinimumSize(QtCore.QSize(318, 0))
        self.rePassword_lineEdit.setStyleSheet("background-color: white")
        self.rePassword_lineEdit.setObjectName("rePassword_lineEdit")
        self.rePasswd_hLayout.addWidget(self.rePassword_lineEdit)
        self.main_vLayout.addLayout(self.rePasswd_hLayout)

        self.contactInfo_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.contactInfo_label.setFont(font)
        self.contactInfo_label.setStyleSheet("color: #B84C6F")
        self.contactInfo_label.setObjectName("contactInfo_label_3")
        self.main_vLayout.addWidget(self.contactInfo_label)

        self.email_hLayout = QtWidgets.QHBoxLayout()
        self.email_hLayout.setObjectName("email_hLayout")
        self.email_label = QtWidgets.QLabel(self.widget)
        self.email_label.setStyleSheet("color: #33423B")
        self.email_label.setObjectName("email_label")
        self.email_label.setFixedWidth(118)
        self.email_hLayout.addWidget(self.email_label)

        self.email_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.email_lineEdit.setStyleSheet("background-color: white")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.email_hLayout.addWidget(self.email_lineEdit)
        self.main_vLayout.addLayout(self.email_hLayout)

        self.reEmail_hLayout = QtWidgets.QHBoxLayout()
        self.reEmail_hLayout.setObjectName("reEmail_hLayout")

        self.reEmail_label = QtWidgets.QLabel(self.widget)
        self.reEmail_label.setStyleSheet("color: #33423B")
        self.reEmail_label.setObjectName("reEmail_label")
        self.reEmail_label.setFixedWidth(118)
        self.reEmail_hLayout.addWidget(self.reEmail_label)

        self.reEmail_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.reEmail_lineEdit.setStyleSheet("background-color: white")
        self.reEmail_lineEdit.setObjectName("reEmail_lineEdit")
        self.reEmail_hLayout.addWidget(self.reEmail_lineEdit)
        self.main_vLayout.addLayout(self.reEmail_hLayout)


        self.cellPhone_hLayout = QtWidgets.QHBoxLayout()
        self.cellPhone_hLayout.setObjectName("cellPhone_hLayout")
        self.cellPhone_label = QtWidgets.QLabel(self.widget)
        self.cellPhone_label.setStyleSheet("color: #33423B")
        self.cellPhone_label.setObjectName("cellPhone_label")
        self.cellPhone_label.setFixedWidth(118)
        self.cellPhone_hLayout.addWidget(self.cellPhone_label)

        self.cellPhone_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.cellPhone_lineEdit.setStyleSheet("background-color: white")
        self.cellPhone_lineEdit.setObjectName("cellPhone_lineEdit")
        self.cellPhone_hLayout.addWidget(self.cellPhone_lineEdit)
        self.main_vLayout.addLayout(self.cellPhone_hLayout)

        self.personal_info_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.personal_info_label.setFont(font)
        self.personal_info_label.setStyleSheet("color: #B84C6F")
        self.personal_info_label.setObjectName("personal_info_label")
        self.main_vLayout.addWidget(self.personal_info_label)

        self.gender_marStatus_hLayout = QtWidgets.QHBoxLayout()
        self.gender_marStatus_hLayout.setObjectName("gender_marStatus_hLayout")

        self.gender_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gender_label.setFont(font)
        self.gender_label.setStyleSheet("color: #B84C6F")
        self.gender_label.setObjectName("gender_label")
        self.gender_marStatus_hLayout.addWidget(self.gender_label)

        self.maritalStatus_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maritalStatus_label.setFont(font)
        self.maritalStatus_label.setStyleSheet("color: #B84C6F")
        self.maritalStatus_label.setObjectName("maritalStatus_label")
        self.gender_marStatus_hLayout.addWidget(self.maritalStatus_label)
        self.main_vLayout.addLayout(self.gender_marStatus_hLayout)

        self.g_ms_hLayout = QtWidgets.QHBoxLayout()
        self.g_ms_hLayout.setObjectName("g_ms_hLayout")

        self.gender_radbtn_hLayout = QtWidgets.QHBoxLayout()
        self.gender_radbtn_hLayout.setObjectName("gender_radbtn_hLayout")

        self.gen_male_radioButton = QtWidgets.QRadioButton(self.widget)
        self.gen_male_radioButton.setStyleSheet("color: #33423B")
        self.gen_male_radioButton.setObjectName("gen_male_radioButton")

        self.gender_radbtn_hLayout.addWidget(self.gen_male_radioButton)
        self.gen_female_radioButton = QtWidgets.QRadioButton(self.widget)
        self.gen_female_radioButton.setStyleSheet("color: #33423B")
        self.gen_female_radioButton.setObjectName("gen_female_radioButton")
        self.gender_radbtn_hLayout.addWidget(self.gen_female_radioButton)

        self.gen_prefNotToSay_radioButton = QtWidgets.QRadioButton(self.widget)
        self.gen_prefNotToSay_radioButton.setStyleSheet("color: #33423B")
        self.gen_prefNotToSay_radioButton.setObjectName("gen_prefNotToSay_radioButton")
        self.gender_radbtn_hLayout.addWidget(self.gen_prefNotToSay_radioButton)

        self.g_ms_hLayout.addLayout(self.gender_radbtn_hLayout)

        self.marStatus_hLayout = QtWidgets.QHBoxLayout()
        self.marStatus_hLayout.setObjectName("marStatus_hLayout")
        self.ms_married_radioButton = QtWidgets.QRadioButton(self.widget)
        self.ms_married_radioButton.setStyleSheet("color: #33423B")
        self.ms_married_radioButton.setObjectName("ms_married_radioButton")
        self.marStatus_hLayout.addWidget(self.ms_married_radioButton)

        self.ms_single_radioButton = QtWidgets.QRadioButton(self.widget)
        self.ms_single_radioButton.setStyleSheet("color: #33423B")
        self.ms_single_radioButton.setObjectName("ms_single_radioButton")
        self.marStatus_hLayout.addWidget(self.ms_single_radioButton)

        self.ms_prefNotToSay_radioButton = QtWidgets.QRadioButton(self.widget)
        self.ms_prefNotToSay_radioButton.setStyleSheet("color: #33423B")
        self.ms_prefNotToSay_radioButton.setObjectName("ms_prefNotToSay_radioButton")
        self.marStatus_hLayout.addWidget(self.ms_prefNotToSay_radioButton)

        self.g_ms_hLayout.addLayout(self.marStatus_hLayout)
        self.main_vLayout.addLayout(self.g_ms_hLayout)

        self.terms_signUp_vLayout = QtWidgets.QVBoxLayout()
        self.terms_signUp_vLayout.setObjectName("terms_signUp_vLayout")

        self.iAgree_pirPolTBox_hLayout = QtWidgets.QHBoxLayout()
        self.iAgree_pirPolTBox_hLayout.setObjectName("iAgree_pirPolTBox_hLayout")

        self.iAgree_vLayout = QtWidgets.QVBoxLayout()
        self.iAgree_vLayout.setObjectName("iAgree_vLayout")
        self.i_agree_checkBox = QtWidgets.QCheckBox(self.widget)
        self.i_agree_checkBox.setText("")
        self.i_agree_checkBox.setObjectName("i_agree_checkBox")
        self.iAgree_vLayout.addWidget(self.i_agree_checkBox)

        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.iAgree_vLayout.addItem(spacerItem)
        self.iAgree_pirPolTBox_hLayout.addLayout(self.iAgree_vLayout)


        self.pir_pol_textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.pir_pol_textBrowser.setStyleSheet("background-color: white; color: #33423B")
        self.pir_pol_textBrowser.setObjectName("pir_pol_textBrowser")
        self.pir_pol_textBrowser.setFixedHeight(50)
        self.iAgree_pirPolTBox_hLayout.addWidget(self.pir_pol_textBrowser)
        self.terms_signUp_vLayout.addLayout(self.iAgree_pirPolTBox_hLayout)

        self.signUp_cancel_hLayout = QtWidgets.QHBoxLayout()
        self.signUp_cancel_hLayout.setObjectName("signUp_cancel_hLayout")
        signUp_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.signUp_cancel_hLayout.addItem(signUp_spacerItem)
        self.singUp_button = QtWidgets.QPushButton(self.widget)
        self.singUp_button.setMinimumSize(QtCore.QSize(180, 0))
        self.singUp_button.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily(".SF NS Display")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.singUp_button.setFont(font)
        self.singUp_button.setMouseTracking(True)
        self.singUp_button.setStyleSheet("background-color: #B84C6F; color: silver")
        self.singUp_button.setObjectName("singUp_button")
        self.signUp_cancel_hLayout.addWidget(self.singUp_button)

        # # ############ Sign Up Button Event ######################
        # self.singUp_button.clicked.connect(self.signUp_btn_event)
        # # ########################################################

        self.cancel_button = QtWidgets.QPushButton(self.widget)
        self.cancel_button.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily(".SF NS Display")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancel_button.setFont(font)
        self.cancel_button.setMouseTracking(True)
        self.cancel_button.setStyleSheet("background-color: rgb(240, 170, 201); color: #8F6F79")
        self.cancel_button.setObjectName("cancel_button")
        self.signUp_cancel_hLayout.addWidget(self.cancel_button)
        self.terms_signUp_vLayout.addLayout(self.signUp_cancel_hLayout)
        self.main_vLayout.addLayout(self.terms_signUp_vLayout)

        # # ############ Cancel Button Event ######################
        # self.cancel_button.clicked.connect(self.cancel_btn_event)
        # # ########################################################

        buttonClick_spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_vLayout.addItem(buttonClick_spacerItem)
        self.button_click_text_area = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.button_click_text_area.setFont(font)
        self.button_click_text_area.setStyleSheet("color: #B84C6F; text-align: center")
        self.button_click_text_area.setText("")
        self.button_click_text_area.setObjectName("button_click_text_area")
        self.main_vLayout.addWidget(self.button_click_text_area)
        MainWindow.setCentralWidget(self.centralwidget)

        # ## Menu Items
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSignup = QtWidgets.QAction(MainWindow)
        self.actionSignup.setObjectName("actionSignup")
        self.actionCancel = QtWidgets.QAction(MainWindow)
        self.actionCancel.setObjectName("actionCancel")
        self.actionQuitForm = QtWidgets.QAction(MainWindow)
        self.actionQuitForm.setObjectName("actionQuit Form")

        self.actionCikis = QtWidgets.QAction(MainWindow)
        self.actionCikis.setObjectName("actionQuit")


        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuFile.addAction(self.actionSignup)
        self.menuFile.addAction(self.actionCancel)
        self.menuFile.addAction(self.actionQuitForm)
        self.menuFile.addAction(self.actionCikis)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # def signUp_btn_event(self):
    #     self.button_click_text_area.setText("Your account is created!")
    #
    # def cancel_btn_event(self):
    #     self.button_click_text_area.setText("You canceled your registration!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uRegForm_label.setText(_translate("MainWindow", "USER REGISTRATION FORM"))
        self.account_label.setText(_translate("MainWindow", "Account"))
        self.firstName_label.setText(_translate("MainWindow", "First Name (*)"))
        self.lastName_label.setText(_translate("MainWindow", "Last Name (*)"))
        self.password_label.setText(_translate("MainWindow", "Password(*)"))
        self.rePassword_label.setText(_translate("MainWindow", "Retype Password(*)"))
        self.contactInfo_label.setText(_translate("MainWindow", "Contact Information"))
        self.email_label.setText(_translate("MainWindow", "E-Mail"))
        self.reEmail_label.setText(_translate("MainWindow", "Retype E-Mail"))
        self.cellPhone_label.setText(_translate("MainWindow", "Cell Phone No"))
        self.personal_info_label.setText(_translate("MainWindow", "Personal Information"))
        self.gender_label.setText(_translate("MainWindow", "Gender"))
        self.maritalStatus_label.setText(_translate("MainWindow", "Marital Status"))
        self.gen_male_radioButton.setText(_translate("MainWindow", "Male"))
        self.gen_female_radioButton.setText(_translate("MainWindow", "Female"))
        self.gen_prefNotToSay_radioButton.setText(_translate("MainWindow", "Prefer not to say"))
        self.ms_married_radioButton.setText(_translate("MainWindow", "Married"))
        self.ms_single_radioButton.setText(_translate("MainWindow", "Single"))
        self.ms_prefNotToSay_radioButton.setText(_translate("MainWindow", "Prefer not to say"))
        self.pir_pol_textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">By clicking this checkbox, you agree to our Terms. Learn how we collect, use and share your data in our Data Policy and how we use cookies and similar technology in our Cookies Policy. You may receive SMS Notifications from us and can opt out any time.</span></p></body></html>"))
        self.singUp_button.setText(_translate("MainWindow", "Sign Up"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSignup.setText(_translate("MainWindow", "Sign Up"))
        self.actionSignup.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCancel.setText(_translate("MainWindow", "Cancel"))
        self.actionCancel.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionQuitForm.setText(_translate("MainWindow", "Quit Form"))
        self.actionQuitForm.setShortcut("Ctrl+Q")

        self.actionCikis.setText(_translate("MainWindow", " Quit "))
        self.actionCikis.setShortcut("Ctrl+Shift+C")


        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_In.setShortcut(_translate("MainWindow", "Ctrl+Shift+="))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
