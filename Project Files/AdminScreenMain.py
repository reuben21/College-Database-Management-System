from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap
import pymysql
from datetime import datetime
# import boto3
# from botocore.exceptions import NoCredentialsError
from urllib.request import urlopen
import random
import smtplib 
import math
import re
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from UpdateProfile import Ui_DialogProfile
from TeacherUpdate import Ui_DialogTeacher
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import images_rc
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

global host,port,dbname,user,passwordDataBase
host="localhost";port=3306;dbname="studentDBMS";user="root";passwordDataBase="reuben"
class Ui_AdminScreen(object):
    def __init__(self,admin_username,admin_password):
        global host,port,dbname,user,passwordDataBase
        self.admin_username=admin_username
        self.admin_password=admin_password
        
        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        cursor=conn.cursor()
        query="SELECT * FROM studentDBMS.administrator WHERE Admin_Username=%s and Admin_Password=%s"
        args=(self.admin_username,self.admin_password)
        cursor.execute(query,args)
        records=cursor.fetchall()
        self.adminPhoneNumber123=records[0][2]
        self.adminEmail=records[0][3]
        self.admin_FN=records[0][4]
        # print(self.adminEmail,self.admin_FN)

    def setupUi(self, AdminScreen):
        AdminScreen.setObjectName("AdminScreen")
        AdminScreen.resize(1155, 669)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/education.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdminScreen.setWindowIcon(icon)
        AdminScreen.setStyleSheet("background-color:#c5eff7;")
        self.AdminWelcomeBtn = QtWidgets.QPushButton(AdminScreen)
        self.AdminWelcomeBtn.setGeometry(QtCore.QRect(320, 10, 511, 41))
        self.AdminWelcomeBtn.setStyleSheet("border: 1px solid #1e8bc3;\n"
        "color:#1e8bc3;\n"
        "border-radius: 10px;\n"
        "font: 75 14pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-microsoft-admin-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminWelcomeBtn.setIcon(icon1)
        self.AdminWelcomeBtn.setIconSize(QtCore.QSize(40, 40))
        self.AdminWelcomeBtn.setObjectName("AdminWelcomeBtn")
        self.AdminScreenTabs = QtWidgets.QTabWidget(AdminScreen)
        self.AdminScreenTabs.setGeometry(QtCore.QRect(20, 70, 1121, 581))
        self.AdminScreenTabs.setAutoFillBackground(False)
        self.AdminScreenTabs.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 10px;\n"
"border:1px solid #c5eff7;\n"
"")
        self.AdminScreenTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.AdminScreenTabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.AdminScreenTabs.setIconSize(QtCore.QSize(30, 30))
        self.AdminScreenTabs.setObjectName("AdminScreenTabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.WelcomeLabelAdmin = QtWidgets.QLabel(self.tab)
        self.WelcomeLabelAdmin.setGeometry(QtCore.QRect(330, 70, 441, 51))
        self.WelcomeLabelAdmin.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.WelcomeLabelAdmin.setObjectName("WelcomeLabelAdmin")
        self.Email_id = QtWidgets.QLabel(self.tab)
        self.Email_id.setGeometry(QtCore.QRect(320, 230, 91, 31))
        self.Email_id.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Email_id.setObjectName("Email_id")
        self.adminPhoneLabel = QtWidgets.QLabel(self.tab)
        self.adminPhoneLabel.setGeometry(QtCore.QRect(320, 290, 151, 41))
        self.adminPhoneLabel.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.adminPhoneLabel.setObjectName("adminPhoneLabel")
        self.AdminPasswordLabel = QtWidgets.QLabel(self.tab)
        self.AdminPasswordLabel.setGeometry(QtCore.QRect(320, 170, 91, 31))
        self.AdminPasswordLabel.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.AdminPasswordLabel.setObjectName("AdminPasswordLabel")
        self.PasswordInput = QtWidgets.QLineEdit(self.tab)
        self.PasswordInput.setGeometry(QtCore.QRect(490, 169, 291, 31))
        self.PasswordInput.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.PasswordInput.setObjectName("PasswordInput")
        self.admin_Email_id = QtWidgets.QLineEdit(self.tab)
        self.admin_Email_id.setGeometry(QtCore.QRect(490, 230, 291, 31))
        self.admin_Email_id.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.admin_Email_id.setObjectName("admin_Email_id")
        self.adminPhoneNumber = QtWidgets.QLineEdit(self.tab)
        self.adminPhoneNumber.setGeometry(QtCore.QRect(490, 300, 291, 31))
        self.adminPhoneNumber.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.adminPhoneNumber.setObjectName("adminPhoneNumber")
        self.UpdateProfileAdminBtn = QtWidgets.QPushButton(self.tab)
        self.UpdateProfileAdminBtn.setGeometry(QtCore.QRect(420, 390, 281, 41))
        self.UpdateProfileAdminBtn.setMouseTracking(True)
        self.UpdateProfileAdminBtn.setTabletTracking(True)

        self.UpdateProfileAdminBtn.setAutoFillBackground(False)
        self.UpdateProfileAdminBtn.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-update-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpdateProfileAdminBtn.setIcon(icon2)
        self.UpdateProfileAdminBtn.setIconSize(QtCore.QSize(40, 40))
        self.UpdateProfileAdminBtn.setObjectName("UpdateProfileAdminBtn")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(310, 50, 481, 451))
        self.label_4.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.WelcomeLabelAdmin.raise_()
        self.Email_id.raise_()
        self.adminPhoneLabel.raise_()
        self.AdminPasswordLabel.raise_()
        self.PasswordInput.raise_()
        self.admin_Email_id.raise_()
        self.adminPhoneNumber.raise_()
        self.UpdateProfileAdminBtn.raise_()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-user-menu-female-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.tab, icon3, "")
        self.Add_Teacher = QtWidgets.QWidget()
        self.Add_Teacher.setObjectName("Add_Teacher")
        self.email_id_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.email_id_2.setGeometry(QtCore.QRect(80, 320, 81, 19))
        self.email_id_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.email_id_2.setObjectName("email_id_2")
        self.email_id = QtWidgets.QLineEdit(self.Add_Teacher)
        self.email_id.setGeometry(QtCore.QRect(250, 320, 191, 31))
        self.email_id.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.email_id.setObjectName("email_id")
        self.re_password = QtWidgets.QLineEdit(self.Add_Teacher)
        self.re_password.setGeometry(QtCore.QRect(250, 270, 191, 31))
        self.re_password.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.re_password.setObjectName("re_password")
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.FEMALE = QtWidgets.QRadioButton(self.Add_Teacher)
        self.FEMALE.setGeometry(QtCore.QRect(320, 180, 61, 17))
        self.FEMALE.setStyleSheet("color:#1e8bc3;")
        self.FEMALE.setObjectName("FEMALE")
        self.gender = QtWidgets.QLabel(self.Add_Teacher)
        self.gender.setGeometry(QtCore.QRect(80, 180, 71, 19))
        self.gender.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.gender.setObjectName("gender")
        self.UploadPicture = QtWidgets.QPushButton(self.Add_Teacher)
        self.UploadPicture.setGeometry(QtCore.QRect(620, 180, 151, 41))
        self.UploadPicture.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.UploadPicture.setObjectName("UploadPicture")
        self.dateofbirth = QtWidgets.QDateEdit(self.Add_Teacher)
        self.dateofbirth.setGeometry(QtCore.QRect(600, 270, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.dateofbirth.setFont(font)
        self.dateofbirth.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateofbirth.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dateofbirth.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dateofbirth.setWrapping(True)
        self.dateofbirth.setAlignment(QtCore.Qt.AlignCenter)
        self.dateofbirth.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateofbirth.setAccelerated(True)
        self.dateofbirth.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateofbirth.setProperty("showGroupSeparator", True)
        self.dateofbirth.setObjectName("dateofbirth")
        self.dateofbirthLabel = QtWidgets.QLabel(self.Add_Teacher)
        self.dateofbirthLabel.setGeometry(QtCore.QRect(470, 270, 121, 19))

        self.dateofbirthLabel.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirthLabel.setObjectName("dateofbirthLabel")
        self.address = QtWidgets.QLabel(self.Add_Teacher)
        self.address.setGeometry(QtCore.QRect(80, 80, 71, 19))
   
        self.address.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.address.setObjectName("address")
        self.full_name = QtWidgets.QLabel(self.Add_Teacher)
        self.full_name.setGeometry(QtCore.QRect(80, 20, 91, 19))
        self.full_name.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name.setObjectName("full_name")
        self.qualification = QtWidgets.QComboBox(self.Add_Teacher)
        self.qualification.setGeometry(QtCore.QRect(600, 320, 241, 31))
        self.qualification.setToolTipDuration(-1)
        self.qualification.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.qualification.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.qualification.setIconSize(QtCore.QSize(10, 10))
        self.qualification.setObjectName("qualification")
        self.qualification.addItem("")
        self.qualification.addItem("")
        self.qualification.addItem("")
        self.qualification.addItem("")
        self.label_10 = QtWidgets.QLabel(self.Add_Teacher)
        self.label_10.setGeometry(QtCore.QRect(70, 430, 111, 31))
        self.label_10.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.Add_Teacher)
        self.label_9.setGeometry(QtCore.QRect(470, 380, 111, 19))
        self.label_9.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.phone_number_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.phone_number_2.setGeometry(QtCore.QRect(80, 370, 131, 19))
        self.phone_number_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.phone_number_2.setObjectName("phone_number_2")
        self.OTHERS = QtWidgets.QRadioButton(self.Add_Teacher)
        self.OTHERS.setGeometry(QtCore.QRect(390, 180, 61, 17))
        self.OTHERS.setStyleSheet("color:#1e8bc3;")
        self.OTHERS.setObjectName("OTHERS")
        self.ImageLabel = QtWidgets.QLabel(self.Add_Teacher)
        self.ImageLabel.setGeometry(QtCore.QRect(640, 20, 111, 151))
        self.ImageLabel.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.ImageLabel.setText("")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.Qulaification = QtWidgets.QLabel(self.Add_Teacher)
        self.Qulaification.setGeometry(QtCore.QRect(470, 320, 121, 31))
        self.Qulaification.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Qulaification.setObjectName("Qulaification")
        self.fullname = QtWidgets.QLineEdit(self.Add_Teacher)
        self.fullname.setGeometry(QtCore.QRect(250, 20, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullname.sizePolicy().hasHeightForWidth())
        self.fullname.setSizePolicy(sizePolicy)
        self.fullname.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.fullname.setObjectName("fullname")
        self.Experience = QtWidgets.QComboBox(self.Add_Teacher)
        self.Experience.setGeometry(QtCore.QRect(250, 430, 191, 31))
        self.Experience.setToolTipDuration(-1)
        self.Experience.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Experience.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.Experience.setIconSize(QtCore.QSize(10, 10))
        self.Experience.setObjectName("Experience")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.Experience.addItem("")
        self.MALE = QtWidgets.QRadioButton(self.Add_Teacher)
        self.MALE.setGeometry(QtCore.QRect(260, 180, 51, 17))
        self.MALE.setStyleSheet("color:#1e8bc3;")
        self.MALE.setObjectName("MALE")
        self.password_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.password_2.setGeometry(QtCore.QRect(80, 220, 91, 19))
        self.password_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.password_2.setObjectName("password_2")
        self.Address = QtWidgets.QTextEdit(self.Add_Teacher)
        self.Address.setGeometry(QtCore.QRect(250, 70, 191, 81))
        self.Address.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Address.setObjectName("Address")
        self.re_passwordlabel = QtWidgets.QLabel(self.Add_Teacher)
        self.re_passwordlabel.setGeometry(QtCore.QRect(80, 270, 161, 19))
        self.re_passwordlabel.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.re_passwordlabel.setObjectName("re_passwordlabel")
        self.password = QtWidgets.QLineEdit(self.Add_Teacher)
        self.password.setGeometry(QtCore.QRect(250, 220, 191, 31))
        self.password.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.phone_number = QtWidgets.QLineEdit(self.Add_Teacher)
        self.phone_number.setGeometry(QtCore.QRect(250, 370, 191, 31))
        self.phone_number.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.phone_number.setObjectName("phone_number")
        self.dept = QtWidgets.QComboBox(self.Add_Teacher)
        self.dept.setGeometry(QtCore.QRect(600, 380, 241, 31))
        self.dept.setToolTipDuration(-1)
        self.dept.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dept.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.dept.setIconSize(QtCore.QSize(10, 10))
        self.dept.setObjectName("dept")

        self.SubmitTeacherForm = QtWidgets.QPushButton(self.Add_Teacher)
        self.SubmitTeacherForm.setGeometry(QtCore.QRect(470, 470, 181, 41))
        self.SubmitTeacherForm.setMouseTracking(True)
        self.SubmitTeacherForm.setTabletTracking(True)

        self.SubmitTeacherForm.setAutoFillBackground(False)
        self.SubmitTeacherForm.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 20pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SubmitTeacherForm.setIcon(icon4)
        self.SubmitTeacherForm.setIconSize(QtCore.QSize(30, 30))
        self.SubmitTeacherForm.setObjectName("SubmitTeacherForm")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-add-administrator-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.Add_Teacher, icon5, "")
        self.teacher_Details = QtWidgets.QWidget()
        self.teacher_Details.setObjectName("teacher_Details")
        self.TeacherDetails = QtWidgets.QTableWidget(self.teacher_Details)
        self.TeacherDetails.setGeometry(QtCore.QRect(10, 40, 731, 491))
        self.TeacherDetails.setStyleSheet("Background:white;\n"
"border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.TeacherDetails.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.TeacherDetails.setRowCount(5)
        self.TeacherDetails.setObjectName("TeacherDetails")
        self.TeacherDetails.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.TeacherDetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TeacherDetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TeacherDetails.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TeacherDetails.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TeacherDetails.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TeacherDetails.setHorizontalHeaderItem(5, item)
        self.TeacherDetails.horizontalHeader().setMinimumSectionSize(33)
        self.Refresh_Teacher = QtWidgets.QPushButton(self.teacher_Details)
        self.Refresh_Teacher.setGeometry(QtCore.QRect(760, 40, 51, 41))
        self.Refresh_Teacher.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Refresh_Teacher.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-refresh-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Refresh_Teacher.setIcon(icon6)
        self.Refresh_Teacher.setIconSize(QtCore.QSize(30, 30))
        self.Refresh_Teacher.setObjectName("Refresh_Teacher")
        self.label_5 = QtWidgets.QLabel(self.teacher_Details)
        self.label_5.setGeometry(QtCore.QRect(790, 420, 181, 101))
        self.label_5.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-teacher-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.teacher_Details, icon7, "")
        self.Student_details = QtWidgets.QWidget()
        self.Student_details.setObjectName("Student_details")
        self.studentDetails = QtWidgets.QTableWidget(self.Student_details)
        self.studentDetails.setGeometry(QtCore.QRect(10, 40, 731, 491))
        self.studentDetails.setStyleSheet("Background:white;\n"
"border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.studentDetails.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.studentDetails.setRowCount(5)
        self.studentDetails.setObjectName("studentDetails")
        self.studentDetails.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentDetails.setHorizontalHeaderItem(6, item)
        self.studentDetails.horizontalHeader().setMinimumSectionSize(33)
        self.Refresh_Student = QtWidgets.QPushButton(self.Student_details)
        self.Refresh_Student.setGeometry(QtCore.QRect(750, 40, 51, 41))
        self.Refresh_Student.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Refresh_Student.setText("")
        self.Refresh_Student.setIcon(icon6)
        self.Refresh_Student.setIconSize(QtCore.QSize(30, 30))
        self.Refresh_Student.setObjectName("Refresh_Student")
        self.label_6 = QtWidgets.QLabel(self.Student_details)
        self.label_6.setGeometry(QtCore.QRect(770, 350, 301, 131))
        self.label_6.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-student-male-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.Student_details, icon8, "")
        self.Add_Course = QtWidgets.QWidget()
        self.Add_Course.setObjectName("Add_Course")
        self.course_id_Input = QtWidgets.QLineEdit(self.Add_Course)
        self.course_id_Input.setGeometry(QtCore.QRect(520, 180, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_id_Input.sizePolicy().hasHeightForWidth())
        self.course_id_Input.setSizePolicy(sizePolicy)
        self.course_id_Input.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.course_id_Input.setObjectName("course_id_Input")
        self.Course_ID_Label = QtWidgets.QLabel(self.Add_Course)
        self.Course_ID_Label.setGeometry(QtCore.QRect(380, 180, 101, 21))

        self.Course_ID_Label.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Course_ID_Label.setObjectName("Course_ID_Label")
        self.AddCourse = QtWidgets.QPushButton(self.Add_Course)
        self.AddCourse.setGeometry(QtCore.QRect(340, 70, 441, 61))
        self.AddCourse.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-course-80.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddCourse.setIcon(icon9)
        self.AddCourse.setIconSize(QtCore.QSize(50, 50))
        self.AddCourse.setObjectName("AddCourse")
        self.Course_Name = QtWidgets.QLabel(self.Add_Course)
        self.Course_Name.setGeometry(QtCore.QRect(380, 240, 131, 31))
        self.Course_Name.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Course_Name.setObjectName("Course_Name")
        self.course_name_in = QtWidgets.QLineEdit(self.Add_Course)
        self.course_name_in.setGeometry(QtCore.QRect(520, 240, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.course_name_in.sizePolicy().hasHeightForWidth())
        self.course_name_in.setSizePolicy(sizePolicy)
        self.course_name_in.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.course_name_in.setObjectName("course_name_in")
        self.add_course_button = QtWidgets.QPushButton(self.Add_Course)
        self.add_course_button.setGeometry(QtCore.QRect(470, 410, 211, 51))
        self.add_course_button.setMouseTracking(True)
        self.add_course_button.setTabletTracking(True)

        self.add_course_button.setAutoFillBackground(False)
        self.add_course_button.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-course-assign-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_course_button.setIcon(icon10)
        self.add_course_button.setIconSize(QtCore.QSize(30, 30))
        self.add_course_button.setObjectName("add_course_button")
        self.depatLabel = QtWidgets.QLabel(self.Add_Course)
        self.depatLabel.setGeometry(QtCore.QRect(380, 300, 131, 31))
        self.depatLabel.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.depatLabel.setObjectName("depatLabel")
        self.deptIn = QtWidgets.QComboBox(self.Add_Course)
        self.deptIn.setGeometry(QtCore.QRect(520, 300, 191, 31))
        self.deptIn.setToolTipDuration(-1)
        self.deptIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.deptIn.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.deptIn.setIconSize(QtCore.QSize(10, 10))
        self.deptIn.setObjectName("deptIn")
        self.label_3 = QtWidgets.QLabel(self.Add_Course)
        self.label_3.setGeometry(QtCore.QRect(320, 50, 481, 451))
        self.label_3.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.course_id_Input.raise_()
        self.Course_ID_Label.raise_()
        self.AddCourse.raise_()
        self.Course_Name.raise_()
        self.course_name_in.raise_()
        self.add_course_button.raise_()
        self.depatLabel.raise_()
        self.deptIn.raise_()
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-course-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.Add_Course, icon11, "")
        self.Alot_Courses = QtWidgets.QWidget()
        self.Alot_Courses.setObjectName("Alot_Courses")
        self.Course_id = QtWidgets.QLabel(self.Alot_Courses)
        self.Course_id.setGeometry(QtCore.QRect(60, 250, 101, 21))

        self.Course_id.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Course_id.setObjectName("Course_id")
        self.course_id_In = QtWidgets.QComboBox(self.Alot_Courses)
        self.course_id_In.setGeometry(QtCore.QRect(230, 250, 211, 31))
        self.course_id_In.setToolTipDuration(-1)
        self.course_id_In.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.course_id_In.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.course_id_In.setIconSize(QtCore.QSize(10, 10))
        self.course_id_In.setObjectName("course_id_In")
        self.faculty_id = QtWidgets.QLabel(self.Alot_Courses)
        self.faculty_id.setGeometry(QtCore.QRect(60, 320, 111, 31))

        self.faculty_id.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.faculty_id.setObjectName("faculty_id")
        self.faculty_ID_IN = QtWidgets.QLineEdit(self.Alot_Courses)
        self.faculty_ID_IN.setGeometry(QtCore.QRect(230, 320, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_ID_IN.sizePolicy().hasHeightForWidth())
        self.faculty_ID_IN.setSizePolicy(sizePolicy)
        self.faculty_ID_IN.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.faculty_ID_IN.setObjectName("faculty_ID_IN")
        self.alotTeacherLabel = QtWidgets.QPushButton(self.Alot_Courses)
        self.alotTeacherLabel.setGeometry(QtCore.QRect(40, 50, 441, 51))
        self.alotTeacherLabel.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-profile-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.alotTeacherLabel.setIcon(icon12)
        self.alotTeacherLabel.setIconSize(QtCore.QSize(50, 50))
        self.alotTeacherLabel.setObjectName("alotTeacherLabel")
        self.AlotCourseBtnTeacher = QtWidgets.QPushButton(self.Alot_Courses)
        self.AlotCourseBtnTeacher.setGeometry(QtCore.QRect(150, 400, 211, 51))
        self.AlotCourseBtnTeacher.setMouseTracking(True)
        self.AlotCourseBtnTeacher.setTabletTracking(True)

        self.AlotCourseBtnTeacher.setAutoFillBackground(False)
        self.AlotCourseBtnTeacher.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-add-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AlotCourseBtnTeacher.setIcon(icon13)
        self.AlotCourseBtnTeacher.setIconSize(QtCore.QSize(30, 30))
        self.AlotCourseBtnTeacher.setObjectName("AlotCourseBtnTeacher")
        self.label = QtWidgets.QLabel(self.Alot_Courses)
        self.label.setGeometry(QtCore.QRect(20, 30, 481, 451))
        self.label.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Alot_Courses)
        self.label_2.setGeometry(QtCore.QRect(600, 30, 481, 451))
        self.label_2.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.course_id_In_Student = QtWidgets.QComboBox(self.Alot_Courses)
        self.course_id_In_Student.setGeometry(QtCore.QRect(790, 260, 211, 31))
        self.course_id_In_Student.setToolTipDuration(-1)
        self.course_id_In_Student.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.course_id_In_Student.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.course_id_In_Student.setIconSize(QtCore.QSize(10, 10))
        self.course_id_In_Student.setObjectName("course_id_In_Student")
        self.Student_In = QtWidgets.QLabel(self.Alot_Courses)
        self.Student_In.setGeometry(QtCore.QRect(630, 330, 111, 31))

        self.Student_In.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Student_In.setObjectName("Student_In")
        self.faculty_ID_IN_Student = QtWidgets.QLineEdit(self.Alot_Courses)
        self.faculty_ID_IN_Student.setGeometry(QtCore.QRect(790, 330, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faculty_ID_IN_Student.sizePolicy().hasHeightForWidth())
        self.faculty_ID_IN_Student.setSizePolicy(sizePolicy)
        self.faculty_ID_IN_Student.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.faculty_ID_IN_Student.setObjectName("faculty_ID_IN_Student")
        self.AlotCourseBtnStudent = QtWidgets.QPushButton(self.Alot_Courses)
        self.AlotCourseBtnStudent.setGeometry(QtCore.QRect(750, 390, 211, 51))
        self.AlotCourseBtnStudent.setMouseTracking(True)
        self.AlotCourseBtnStudent.setTabletTracking(True)

        self.AlotCourseBtnStudent.setAutoFillBackground(False)
        self.AlotCourseBtnStudent.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.AlotCourseBtnStudent.setIcon(icon13)
        self.AlotCourseBtnStudent.setIconSize(QtCore.QSize(30, 30))
        self.AlotCourseBtnStudent.setObjectName("AlotCourseBtnStudent")
        self.Course_id_4 = QtWidgets.QLabel(self.Alot_Courses)
        self.Course_id_4.setGeometry(QtCore.QRect(630, 260, 101, 21))

        self.Course_id_4.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Course_id_4.setObjectName("Course_id_4")
        self.alotStudentLabel = QtWidgets.QPushButton(self.Alot_Courses)
        self.alotStudentLabel.setGeometry(QtCore.QRect(620, 50, 441, 51))
        self.alotStudentLabel.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.alotStudentLabel.setIcon(icon12)
        self.alotStudentLabel.setIconSize(QtCore.QSize(50, 50))
        self.alotStudentLabel.setObjectName("alotStudentLabel")
        self.label_11 = QtWidgets.QLabel(self.Alot_Courses)
        self.label_11.setGeometry(QtCore.QRect(60, 150, 111, 21))
        self.label_11.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.dept_2 = QtWidgets.QComboBox(self.Alot_Courses)
        self.dept_2.setGeometry(QtCore.QRect(230, 150, 211, 31))
        self.dept_2.setToolTipDuration(-1)
        self.dept_2.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dept_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.dept_2.setIconSize(QtCore.QSize(10, 10))
        self.dept_2.setObjectName("dept_2")

        self.dept_3 = QtWidgets.QComboBox(self.Alot_Courses)
        self.dept_3.setGeometry(QtCore.QRect(790, 150, 211, 31))
        self.dept_3.setToolTipDuration(-1)
        self.dept_3.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dept_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.dept_3.setIconSize(QtCore.QSize(10, 10))
        self.dept_3.setObjectName("dept_3")
        self.label_12 = QtWidgets.QLabel(self.Alot_Courses)
        self.label_12.setGeometry(QtCore.QRect(620, 140, 111, 31))
        self.label_12.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.Get_Course_Teacher = QtWidgets.QPushButton(self.Alot_Courses)
        self.Get_Course_Teacher.setGeometry(QtCore.QRect(260, 200, 121, 31))
        self.Get_Course_Teacher.setMouseTracking(True)
        self.Get_Course_Teacher.setTabletTracking(True)

        self.Get_Course_Teacher.setAutoFillBackground(False)
        self.Get_Course_Teacher.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Get_Course_Teacher.setIcon(icon13)
        self.Get_Course_Teacher.setIconSize(QtCore.QSize(0, 0))
        self.Get_Course_Teacher.setObjectName("Get_Course_Teacher")
        self.Get_Course_Student = QtWidgets.QPushButton(self.Alot_Courses)
        self.Get_Course_Student.setGeometry(QtCore.QRect(830, 200, 121, 31))
        self.Get_Course_Student.setMouseTracking(True)
        self.Get_Course_Student.setTabletTracking(True)
 
        self.Get_Course_Student.setAutoFillBackground(False)
        self.Get_Course_Student.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Get_Course_Student.setIcon(icon13)
        self.Get_Course_Student.setIconSize(QtCore.QSize(0, 0))
        self.Get_Course_Student.setObjectName("Get_Course_Student")
        self.label.raise_()
        self.Course_id.raise_()
        self.course_id_In.raise_()
        self.faculty_id.raise_()
        self.faculty_ID_IN.raise_()
        self.alotTeacherLabel.raise_()
        self.AlotCourseBtnTeacher.raise_()
        self.label_2.raise_()
        self.course_id_In_Student.raise_()
        self.Student_In.raise_()
        self.faculty_ID_IN_Student.raise_()
        self.AlotCourseBtnStudent.raise_()
        self.Course_id_4.raise_()
        self.alotStudentLabel.raise_()
        self.label_11.raise_()
        self.dept_2.raise_()
        self.dept_3.raise_()
        self.label_12.raise_()
        self.Get_Course_Teacher.raise_()
        self.Get_Course_Student.raise_()
        self.AdminScreenTabs.addTab(self.Alot_Courses, icon12, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.AdminPasswordLabel_2 = QtWidgets.QLabel(self.tab_2)
        self.AdminPasswordLabel_2.setGeometry(QtCore.QRect(20, 20, 191, 41))
        self.AdminPasswordLabel_2.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.AdminPasswordLabel_2.setObjectName("AdminPasswordLabel_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 90, 991, 421))
        self.listWidget.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")
        self.RefreshFeedback = QtWidgets.QPushButton(self.tab_2)
        self.RefreshFeedback.setGeometry(QtCore.QRect(1020, 20, 51, 41))
        self.RefreshFeedback.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.RefreshFeedback.setText("")
        self.RefreshFeedback.setIcon(icon6)
        self.RefreshFeedback.setIconSize(QtCore.QSize(30, 30))
        self.RefreshFeedback.setObjectName("RefreshFeedback")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-feedback-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.tab_2, icon14, "")

        
        self.MALE.setChecked(True)
        self.UpdateProfileAdminBtn.clicked.connect(self.UpdateAdminDetails)
        self.SubmitTeacherForm.clicked.connect(self.SubmitDetails)        
        self.Refresh_Teacher.clicked.connect(self.LoadIntoTable)
        self.LoadIntoTable(self.admin_FN)
        self.LoadIntoTableStudent(self.admin_FN)
        self.AlotCourseBtnTeacher.clicked.connect(self.alotcourseT)
        self.Refresh_Student.clicked.connect(self.LoadIntoTableStudent)
        self.add_course_button.clicked.connect(self.add_course)
        
        self.Get_Course_Teacher.clicked.connect(self.RefreshCoursesFunT)
        self.Get_Course_Student.clicked.connect(self.RefreshCoursesFunS)
        self.UploadPicture.clicked.connect(self.openImage)
        self.AlotCourseBtnStudent.clicked.connect(self.alotcourseS)
        self.retranslateUi(AdminScreen)
        self.GetCoursesListFeeback(self.admin_FN)
        self.RefreshFeedback.clicked.connect(self.GetCoursesListFeeback)
        self.studentDetails.cellClicked.connect(self.cell_was_clicked_Student_Table)
        self.TeacherDetails.cellClicked.connect(self.cell_was_clicked_Teacher_Table)
    
        self.AdminScreenTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminScreen)

    def retranslateUi(self, AdminScreen):
        global host,port,dbname,user,passwordDataBase
        _translate = QtCore.QCoreApplication.translate
        AdminScreen.setWindowTitle(_translate("AdminScreen", f"Admin Screen Of {self.admin_FN}"))
        self.AdminWelcomeBtn.setText(_translate("AdminScreen", f"Welcome Adminstrator,{self.admin_FN}"))
        self.WelcomeLabelAdmin.setText(_translate("AdminScreen", f"  Welcome  ,{self.admin_FN}"))
        self.Email_id.setText(_translate("AdminScreen", "Email ID:"))
        self.adminPhoneLabel.setText(_translate("AdminScreen", "Phone Number:"))
        self.AdminPasswordLabel.setText(_translate("AdminScreen", "Password:"))
        self.UpdateProfileAdminBtn.setText(_translate("AdminScreen", "UPDATE PROFILE"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.tab), _translate("AdminScreen", "Welcome Admin"))
        self.email_id_2.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Email-ID</span></p></body></html>"))
        self.FEMALE.setText(_translate("AdminScreen", "FEMALE"))
        self.gender.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Gender</span></p></body></html>"))
        self.UploadPicture.setText(_translate("AdminScreen", "Upload Picture"))
        self.dateofbirthLabel.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Date Of Birth</span></p></body></html>"))
        self.address.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Address</span></p></body></html>"))
        self.full_name.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.qualification.setItemText(0, _translate("AdminScreen", "-----Qualification-----"))
        self.qualification.setItemText(1, _translate("AdminScreen", "Bachelor of Engineering "))
        self.qualification.setItemText(2, _translate("AdminScreen", "Master of Engineering "))
        self.qualification.setItemText(3, _translate("AdminScreen", "PhD in Engineering"))
        self.label_10.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Experience</span></p></body></html>"))
        self.label_9.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Department</span></p></body></html>"))
        self.phone_number_2.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        self.OTHERS.setText(_translate("AdminScreen", "OTHERS"))
        self.Qulaification.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Qualification</span></p></body></html>"))


        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)


        self.Experience.setItemText(0, _translate("AdminScreen", "----Experience----"))
        self.Experience.setItemText(1, _translate("AdminScreen", "1 Year"))
        self.Experience.setItemText(2, _translate("AdminScreen", "2 Years"))
        self.Experience.setItemText(3, _translate("AdminScreen", "3 Years"))
        self.Experience.setItemText(4, _translate("AdminScreen", "4 Years"))
        self.Experience.setItemText(5, _translate("AdminScreen", "5 Years"))
        self.Experience.setItemText(6, _translate("AdminScreen", "More Than 5 Years"))
        self.Experience.setItemText(7, _translate("AdminScreen", "More Than 10 Years"))
        self.MALE.setText(_translate("AdminScreen", "MALE"))
        self.password_2.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.re_passwordlabel.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Re-Enter Password</span></p></body></html>"))
        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT dept_id FROM studentdbms.department;"
        cursor.execute(query)
        result=cursor.fetchall()
        self.dept.addItem("")
        self.dept.setItemText(0, _translate("AdminScreen", "----Department----"))
        for i in range(1,len(result)):
                self.dept.addItem("")
                self.dept.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))
        self.deptIn.addItem("")
        self.deptIn.setItemText(0, _translate("AdminScreen", "----Department----"))
        for i in range(1,len(result)):
                self.deptIn.addItem("")
                self.deptIn.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))
        
        self.dept_2.addItem("")
        self.dept_2.setItemText(0, _translate("AdminScreen", "----Department----"))
        for i in range(1,len(result)):
                self.dept_2.addItem("")
                self.dept_2.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))
        self.SubmitTeacherForm.setText(_translate("AdminScreen", "SUBMIT"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.Add_Teacher), _translate("AdminScreen", "Add Teacher"))
        self.dept_3.addItem("")
        self.dept_3.setItemText(0, _translate("AdminScreen", "----Department----"))
        for i in range(1,len(result)):
                self.dept_3.addItem("")
                self.dept_3.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))        
        item = self.TeacherDetails.horizontalHeaderItem(0)
        item.setText(_translate("AdminScreen", "Faculty ID"))
        item = self.TeacherDetails.horizontalHeaderItem(1)
        item.setText(_translate("AdminScreen", "Full Name"))
        item = self.TeacherDetails.horizontalHeaderItem(2)
        item.setText(_translate("AdminScreen", "Phone No"))
        item = self.TeacherDetails.horizontalHeaderItem(3)
        item.setText(_translate("AdminScreen", "Email-ID"))
        item = self.TeacherDetails.horizontalHeaderItem(4)
        item.setText(_translate("AdminScreen", "Dept"))
        item = self.TeacherDetails.horizontalHeaderItem(5)
        item.setText(_translate("AdminScreen", "Gender"))
        self.label_5.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">CLICK ON A FACULTY ID </span></p><p align=\"center\"><span style=\" font-size:9pt;\">TO SEE COMPLETE DETAILS,</span></p><p align=\"center\"><span style=\" font-size:9pt;\">YOU CAN UPDATE,OR DELETE</span></p><p align=\"center\"><span style=\" font-size:9pt;\">AN FACULTY ALSO</span></p><p align=\"center\"><span style=\" font-size:9pt;\"><br/></span></p></body></html>"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.teacher_Details), _translate("AdminScreen", "Teacher Details"))
        item = self.studentDetails.horizontalHeaderItem(0)
        item.setText(_translate("AdminScreen", "PID"))
        item = self.studentDetails.horizontalHeaderItem(1)
        item.setText(_translate("AdminScreen", "Full Name"))
        item = self.studentDetails.horizontalHeaderItem(2)
        item.setText(_translate("AdminScreen", "Phone No"))
        item = self.studentDetails.horizontalHeaderItem(3)
        item.setText(_translate("AdminScreen", "Gender"))
        item = self.studentDetails.horizontalHeaderItem(4)
        item.setText(_translate("AdminScreen", "Email-ID"))
        item = self.studentDetails.horizontalHeaderItem(5)
        item.setText(_translate("AdminScreen", "Dept"))
        item = self.studentDetails.horizontalHeaderItem(6)
        item.setText(_translate("AdminScreen", "Approvals"))
        self.label_6.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">CLICK ON A STUDENT ID </span></p><p align=\"center\"><span style=\" font-size:9pt;\">TO SEE COMPLETE DETAILS,</span></p><p align=\"center\"><span style=\" font-size:9pt;\">YOU CAN UPDATE,OR DELETE STUDENT</span></p><p align=\"center\"><span style=\" font-size:9pt;\">YOU CAN APPROVE STUDENTS </span></p><p align=\"center\"><span style=\" font-size:9pt;\"> BY ALOTTING THEM COURSES</span></p><p align=\"center\"><span style=\" font-size:9pt;\"><br/></span></p></body></html>"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.Student_details), _translate("AdminScreen", "Student Details"))
        self.Course_ID_Label.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.Course_ID_Label.setText(_translate("AdminScreen", "<html><head/><body><p>Course ID:</p></body></html>"))
        self.AddCourse.setText(_translate("AdminScreen", "ADD COURSE"))
        self.Course_Name.setText(_translate("AdminScreen", "<html><head/><body><p>Course Name:</p></body></html>"))
        self.add_course_button.setText(_translate("AdminScreen", "ADD COURSE"))
        self.depatLabel.setText(_translate("AdminScreen", "<html><head/><body><p>Department:</p></body></html>"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.Add_Course), _translate("AdminScreen", "Add Course"))
        self.Course_id.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.Course_id.setText(_translate("AdminScreen", "<html><head/><body><p>Course ID:</p></body></html>"))
        self.faculty_id.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.faculty_id.setText(_translate("AdminScreen", "<html><head/><body><p>Faculty ID:</p></body></html>"))
        self.alotTeacherLabel.setText(_translate("AdminScreen", "ALOTTING COURSES TO TEACHER"))
        self.AlotCourseBtnTeacher.setText(_translate("AdminScreen", "ALOT COURSE"))
        self.Student_In.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.Student_In.setText(_translate("AdminScreen", "<html><head/><body><p>Student ID:</p></body></html>"))
        self.AlotCourseBtnStudent.setText(_translate("AdminScreen", "ALOT COURSE"))
        self.Course_id_4.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.Course_id_4.setText(_translate("AdminScreen", "<html><head/><body><p>Course ID:</p></body></html>"))
        self.alotStudentLabel.setText(_translate("AdminScreen", "ALOTTING COURSES TO STUDENT"))
        self.label_11.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Department:</span></p></body></html>"))
        self.label_12.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Department:</span></p></body></html>"))
        self.Get_Course_Teacher.setText(_translate("AdminScreen", "GET COURSE"))
        self.Get_Course_Student.setText(_translate("AdminScreen", "GET COURSE"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.Alot_Courses), _translate("AdminScreen", "Alot Courses"))
        self.AdminPasswordLabel_2.setText(_translate("AdminScreen", "Feedback Recieved:"))
        self.PasswordInput.setText(_translate("AdminScreen",f"{self.admin_password}"))
        self.admin_Email_id.setText(_translate("AdminScreen",f"{self.adminEmail}"))
        self.adminPhoneNumber.setText(_translate("AdminScreen",f"{self.adminPhoneNumber123}"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.tab_2), _translate("AdminScreen", "View Feedback"))

    def cell_was_clicked_Teacher_Table(self):
        row = self.TeacherDetails.currentItem().row()
        
        col = self.TeacherDetails.currentItem().column()
        col1=self.TeacherDetails.currentItem().text()
        
        print(len(col1))
        item = self.TeacherDetails.horizontalHeaderItem(col).text()
        
        if len(col1)==6 and item=="Faculty ID":
            self.window2=QtWidgets.QDialog()
            self.ui2=Ui_DialogTeacher(col1)
            self.ui2.setupUi(self.window2)
            
            self.window2.show()
            
        else:
            pass

    
    def cell_was_clicked_Student_Table(self):
        row = self.studentDetails.currentItem().row()
        
        col = self.studentDetails.currentItem().column()
        col1=self.studentDetails.currentItem().text()
        
        print(col1)
        item = self.studentDetails.horizontalHeaderItem(col).text()
        
        if len(col1)==6 and item=="PID":
            self.window=QtWidgets.QDialog()
            self.ui=Ui_DialogProfile(col1)
            self.ui.setupUi(self.window)
            
            self.window.show()
            
        else:
            pass
    def GetCoursesListFeeback(self,Fullname=None):
        print(Fullname)
        global host,port,dbname,user,passwordDataBase
        pass
        self.listWidget.clear()
        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        # print("connection successful")
        Query="SELECT course_id, explainantion, Punctuality, Class_Handling, Comments From studentdbms.Feedback;"
        cursor=conn.cursor()
        cursor.execute(Query)
        records=cursor.fetchall()

        CourseFeeb=[]
        for i in range(len(records)):
            CourseFeeb.append(f"Course-ID->{records[i][0]} Explanation->{records[i][1]} Punctuality->{records[i][2]} Class Handling->{records[i][3]} Comments->{records[i][4]}")
        # print(CourseFeeb)
        self.listWidget.addItems(CourseFeeb)
        conn.commit()
        conn.close()

    def RefreshCoursesFunT(self):
        _translate = QtCore.QCoreApplication.translate
        deptId_T=self.dept_2.currentText()

        global host,port,dbname,user,passwordDataBase
        print(deptId_T)
        if deptId_T!="----Department----" and deptId_T!="":
            try:
                self.course_id_In.clear()
                conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                cursor=conn.cursor()
                query = "SELECT course_id,course_name from course where dept_id=%s;"
                cursor.execute(query,str(deptId_T))
                result=cursor.fetchall()
                # print(result)
                if result!=():

                    listOfCourses=[None]
                    for i in range(len(result)):
                            listOfCourses.append(result[i][0]+"--"+result[i][1])
                    self.course_id_In.addItem("")
                    self.course_id_In.setItemText(0, _translate("AdminScreen", "----Course-ID----"))
                    for i in range(1,len(listOfCourses)):
                            self.course_id_In.addItem("")
                            self.course_id_In.setItemText(i, _translate("AdminScreen", f"{listOfCourses[i]}"))
                else:
                    self.course_id_In.clear()
                    self.warning("No Courses","No Courses added in the department")

            except Exception as err:
                self.warning("SQL ERROR",f"{err}")
        else:
            self.warning("Wrong Department","Incorrect Department Selected")
    def RefreshCoursesFunS(self):
        _translate = QtCore.QCoreApplication.translate
        deptId_S=self.dept_3.currentText()
        global host,port,dbname,user,passwordDataBase
        print(deptId_S)
        pass
        if deptId_S!="----Department----" and deptId_S!="":
            try:
                self.course_id_In_Student.clear()
                conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                cursor=conn.cursor()
                query = "SELECT course_id,course_name from course where dept_id=%s;"
                cursor.execute(query,str(deptId_S))
                result=cursor.fetchall()
                # print(result)
                if result!=():

                    listOfCourses=[None,None]
                    for i in range(len(result)):
                            listOfCourses.append(result[i][0]+"--"+result[i][1])
                    
                    self.course_id_In_Student.addItem("")
                    self.course_id_In_Student.addItem("")
                    self.course_id_In_Student.setItemText(0, _translate("AdminScreen", "----Course-ID----"))
                    self.course_id_In_Student.setItemText(1, _translate("AdminScreen", "--ALL COURSES--"))
                    for i in range(2,len(listOfCourses)):
                            self.course_id_In_Student.addItem("")
                            self.course_id_In_Student.setItemText(i, _translate("AdminScreen", f"{listOfCourses[i]}"))
                else:
                    self.course_id_In_Student.clear()
                    self.warning("No Courses","No Courses added in the department")
            except Exception as err:
                self.warning("SQL ERROR",f"{err}")
        else:
            self.warning("Wrong Department","Incorrect Department Selected")
    def add_course(self):
        global host,port,dbname,user,passwordDataBase
        courseid=self.course_id_Input.text()
        coursename=self.course_name_in.text()
        deptCourse=self.deptIn.currentText()
        if courseid and coursename and deptCourse!="----Department----":
            try:
       
                conn1 = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                cursor1=conn1.cursor()
                query5 = "INSERT into studentdbms.course (course_id,course_name,dept_id) VALUES(%s,%s,%s);"
                args=(courseid,coursename,deptCourse)
                cursor1.execute(query5,args)
                conn1.commit()
                conn1.close()
                self.messagebox("Course Added","Course Added Successfully")
            except Exception as err:
                self.warning("SQL ERROR",f"{err}")
        else:
            self.warning("Error","Fileds Found Empty")

    def alotcourseS(self):
        courseId=self.course_id_In_Student.currentText()
        idStudent=self.faculty_ID_IN_Student.text()
        dept=self.dept_3.currentText()
        # print(idStudent,courseId,dept)
        global host,port,dbname,user,passwordDataBase
        connIds = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        cursor2=connIds.cursor()
        qyeryToGetIds="SELECT PID,id_dept FROM studentdbms.student_registration;"
        cursor2.execute(qyeryToGetIds)
        facultyIDs=cursor2.fetchall()
        Stud_ID=[]
        for fi in range(len(facultyIDs)):
            Stud_ID.append(facultyIDs[fi][0])
        cursorForIddeptcheck=connIds.cursor()
        QueryToConfirmID="SELECT id_dept FROM studentdbms.student_registration where PID=%s;"
        cursorForIddeptcheck.execute(QueryToConfirmID,(int(idStudent)))

        dept_check_student=cursorForIddeptcheck.fetchall()
        print(dept_check_student)
        connIds.commit()
        connIds.close()
        approvalApproved="APPROVED"
  
        if courseId and idStudent:
            if courseId!="----Course-ID----":
                if dept!="----Department----":
                    if dept==str(dept_check_student[0][0]):

                        if int(idStudent) in Stud_ID:
                            if courseId=="--ALL COURSES--":
                                try:

                                    conn1A = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                    cursorForapproval=conn1A.cursor()

                                    UpdateAppro="UPDATE student_registration SET Approval=%s where pid=%s"
                                    cursorForapproval.execute(UpdateAppro,(approvalApproved,int(idStudent)))
                                                      
                                    cursor1=conn1A.cursor()
                                    query5 = "SELECT * FROM studentdbms.course where dept_id=%s;"
                                    cursor1.execute(query5,str(dept))
                                    gettingAllotedCourses=cursor1.fetchall()
                                    
                                    conn1A.commit()
                                    conn1A.close()                                
                                    course_ID_List=[]
                                    for record in range(len(gettingAllotedCourses)):
                                        course_ID_List.append(gettingAllotedCourses[record][0])
                                    # print(course_ID_List)

                                    conn2B = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                    cursor2=conn2B.cursor()
                                    queyCourses="SELECT PID,course_id From studentDBMS.takes "
                                    cursor2.execute(queyCourses)
                                    records569=cursor2.fetchall()
                                    # print(records569)
                                    conn2B.commit()
                                    conn2B.close()
                                    conn3B = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                    cursor2C=conn3B.cursor()
                                    queyCourses="SELECT PID,course_id From studentDBMS.exam_scheme; "
                                    cursor2C.execute(queyCourses)
                                    recordOfExams=cursor2C.fetchall()

                                    conn3B.commit()
                                    conn3B.close()

                                    for ins in range(len(course_ID_List)):
                                        conn1 = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                        cursor1=conn1.cursor()
                                        args=(int(idStudent),course_ID_List[ins])
                                        
                                        if args not in records569:
                                            queyCourses="INSERT into studentDBMS.takes (PID,course_id) VALUES (%s,%s)"
                                            cursor1.execute(queyCourses,args)
                                            cursor1.execute(query5,dept)

                                            conn1.commit()
                                            conn1.close()
                                            print("s")                                        
                                        else:
                                            pass
                                            print("F")
                                        if args not in recordOfExams:
                                            conn12 = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                            cursorForExamScheme=conn12.cursor()
                                            examquery="INSERT into studentDBMS.exam_scheme (PID,course_id) VALUES (%s,%s)"
                                            cursorForExamScheme.execute(examquery,args)
                                            conn12.commit()
                                            conn12.close()
                                        else:
                                            pass
                                            print("Exam alotted")


                                    self.messagebox("ALL COUSES","ALL COURSES INSERTED OR HAVE ALREADY BEEN INSERTED")
                                except pymysql.Error as error:
                                    self.warning("ERROR INSERTING",f"{error} OR U havent Added the course Yet")
                            elif courseId!="--ALL COURSES--":
                                args=(int(idStudent),courseId[0:6])
                                conn1 = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                cursor1=conn1.cursor()
                                query5 = "SELECT PID,course_id FROM studentdbms.takes;"
                                cursor1.execute(query5)
                                gettingAllotedCourses=cursor1.fetchall()
                                conn1.commit()
                                conn1.close()
                                conn1A = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                cursorForapproval=conn1A.cursor()

                                UpdateAppro="UPDATE student_registration SET Approval=%s where pid=%s"
                                cursorForapproval.execute(UpdateAppro,(approvalApproved,idStudent))
                                if args in gettingAllotedCourses:
                                        self.warning("Same Course Alotted","You Can Not Allot Same Courses Again")
                                else:
                                        pass
                                        try:    
                                            conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase1, db=dbname)
                                            cursor=conn.cursor()
                                            queyCourses="INSERT into studentDBMS.takes (PID,course_id) VALUES (%s,%s)"
                                            cursor.execute(queyCourses,args)
                                            conn.commit()
                                            conn.close()
                                            self.messagebox("Successful Alotted","Course Alotted Successfully")
                                        except pymysql.Error as error:
                                            self.warning("ERROR INSERTING",f"{error} OR U havent Added the course Yet")


                        else:
                            self.warning("Student ID Error","Student ID Entered is Incorrect")
                    else:
                        self.warning("Student Error","Student Not From Same Department")
                else:
                    self.warning("Department Error","Department Selected is Incorrect")
            else:
                self.warning("Course-ID Error","Course-ID Selected is Incorrect")
        else:
            self.warning("Error ","No Student ID Entered")

    def convertToBinaryData(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
    def alotcourseT(self):
        courseId=self.course_id_In.currentText()
        idFaculty=self.faculty_ID_IN.text()
        dept=self.dept_2.currentText()
        # print(idFaculty,courseId,dept)
        global host,port,dbname,user,passwordDataBase
        connIds = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        cursor2=connIds.cursor()
        qyeryToGetIds="SELECT fac_id FROM studentdbms.faculty;"
        cursor2.execute(qyeryToGetIds)
        facultyIDs=cursor2.fetchall()
        fac_ID=[]
        for fi in range(len(facultyIDs)):
            fac_ID.append(facultyIDs[fi][0])
        # print(fac_ID)
        cursorForIddeptcheck=connIds.cursor()
        QueryToConfirmID="SELECT dept_id FROM studentdbms.faculty where fac_id=%s;"
        cursorForIddeptcheck.execute(QueryToConfirmID,(int(idFaculty)))

        dept_check_Teacher=cursorForIddeptcheck.fetchall()
        connIds.commit()
        connIds.close()
        if courseId and idFaculty:
            if courseId!="----Course-ID----":
                if dept!="----Department----":
                    if dept==str(dept_check_Teacher[0][0]):

                        if int(idFaculty) in fac_ID:

                            args=(int(idFaculty),courseId[0:6])
                            conn1 = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                            cursor1=conn1.cursor()
                            query5 = "SELECT fac_id,course_id FROM studentdbms.teaches;"
                            cursor1.execute(query5)
                            gettingAllotedCourses=cursor1.fetchall()
                            conn1.commit()
                            conn1.close()
                            if args in gettingAllotedCourses:
                                    self.warning("Same Course Alotted","You Can Not Allot Same Courses Again")
                            else:
                                    pass
                                    try:    
                                        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                        cursor=conn.cursor()
                                        queyCourses="INSERT into studentDBMS.teaches (fac_id,course_id) VALUES (%s,%s)"
                                        cursor.execute(queyCourses,args)
                                        conn.commit()
                                        conn.close()
                                        self.messagebox("Successful Alotted","Course Alotted Successfully")
                                    except pymysql.Error as error:
                                        self.warning("ERROR INSERTING",f"{error} OR U havent Added the course Yet")


                        else:
                            self.warning("Faculty ID Error","Faculty ID Entered is Incorrect")
                    else:
                        self.warning("Faculty Error","Faculty Not From Same Department")
                else:
                    self.warning("Department Error","Department Selected is Incorrect")
            else:
                self.warning("Course-ID Error","Course-ID Selected is Incorrect")
        else:
            self.warning("Error ","No Faculty ID Entered")
    def UpdateAdminDetails(self):
        password=self.PasswordInput.text()
        adminEmail=self.admin_Email_id.text()
        phno=self.adminPhoneNumber.text()
        global host,port,dbname,user,passwordDataBase
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        cursor=conn.cursor()
        Qu_Up="UPDATE studentDBMS.administrator SET Admin_Password=%s,admin_phone_no=%s,admin_email_id=%s where Admin_Username=%s"        
        cursor.execute(Qu_Up,(password,phno,adminEmail,self.admin_username))
        conn.commit()
        conn.close()
        self.messagebox("Data Updated ","Data Updated Successfully")

    def LoadIntoTableStudent(self,Fullname="None"):
        print(Fullname)
        global host,port,dbname,user,passwordDataBase
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT PID,full_name,phone_no,gender,email_id,id_dept,Approval FROM studentdbms.student_registration;"
        cursor.execute(query)
        result=cursor.fetchall()
        self.studentDetails.setRowCount(0)
        header=self.studentDetails.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for row_no,row_data in enumerate(result):
            self.studentDetails.insertRow(row_no)
            for column_no,data in enumerate(row_data):
                self.studentDetails.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))    
    def LoadIntoTable(self,Fullname="None"):
        # host="reubendbms.csubdeug2c1q.ap-south-1.rds.amazonaws.com"
        # port=3347
        print(Fullname)
        global host,port,dbname,user,passwordDataBase
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT fac_id,full_name,phone_no,email_id,dept_id,gender FROM studentdbms.faculty;"
        cursor.execute(query)
        result=cursor.fetchall()
        self.TeacherDetails.setRowCount(0)
        header=self.TeacherDetails.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for row_no,row_data in enumerate(result):
            self.TeacherDetails.insertRow(row_no)
            for column_no,data in enumerate(row_data):
                self.TeacherDetails.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))


    def sendEmailDetails(self,receiver_email,otp):


        sender_email = "student.sdbms@gmail.com"
         
        password = "Reuben@21"

        message = MIMEMultipart("alternative")
        message["Subject"] = "One-Time Password Verification"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = f"""\
        <html>
          <body>
            <p><h3>Hello,Thank your for Registering with us.</h3><br>
              <h1>Login Details: \n PID:- {otp[0]} \n Password:- {otp[1]}</h1> 
            </p>
          </body>
        </html>
        """

        part2 = MIMEText(html, "html")

        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        self.messagebox("Details Sent ",f"The PID and Password has been send To Your Email:{receiver_email}")
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('education.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    
    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('education.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def openImage(self):
        global strimg
        self.url=QFileDialog.getOpenFileName()
        strimg=str(self.url[0])
        self.ImageLabel.setPixmap(QtGui.QPixmap(strimg))
     
    def SubmitDetails(self):
        global strimg
        global urlofImage
        global host,port,dbname,user,passwordDataBase
        fullnameIn=self.fullname.text()
        passwordIn=self.password.text()
        repasswordIn=self.re_password.text()
        addressIn=self.Address.toPlainText()
        dobIn=self.dateofbirth.date().toPyDate()
        phNumberIn=self.phone_number.text()
        emailidIn=self.email_id.text()
        qualifIn=self.qualification.currentText()
        experIn=self.Experience.currentText()
        
        if self.MALE.isChecked():
            genderIn="Male"
        elif self.FEMALE.isChecked():
            genderIn="Female"
        elif self.OTHERS.isChecked():
            genderIn="Others"
        deptIn=self.dept.currentText()
        print(fullnameIn,passwordIn,repasswordIn,addressIn,dobIn,phNumberIn,emailidIn,genderIn,deptIn)

        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

        
        pass

        if fullnameIn and addressIn and emailidIn and phNumberIn and repasswordIn and passwordIn and genderIn and dobIn and deptIn and qualifIn and experIn:
            if strimg!="":
                pass
                if re.match("^([a-zA-Z]+|[a-zA-Z]+\s{1}[a-zA-Z]{1,}|[a-zA-Z]+\s{1}[a-zA-Z]{3,}\s{1}[a-zA-Z]{1,})$",fullnameIn):
                    pass

                    if re.match("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$",emailidIn): # validating the email 
                        pass
                        if re.match("\+?\d[\d -]{8,12}\d",phNumberIn):
                            pass
                            if passwordIn == repasswordIn:
                                pass
                                if qualifIn !="-----Qualification-----":
                                    pass
                                    if experIn !="----Experience----":
                                        pass
                                        if deptIn !="----Department----":
                                                                         
                                            try:
                                                # host="reubendbms.csubdeug2c1q.ap-south-1.rds.amazonaws.com"
                                                
                                                if "a"=="a":
                                                    # print("a\n\n\n") 
                                                    if "a"=="a":
                                                        
                                                        empPicture = self.convertToBinaryData(strimg)

                                                        conn = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                                        print("connection successful")
                                                        cursor=conn.cursor()
                                                        args=(str(passwordIn),str(deptIn),str(qualifIn),dobIn,str(fullnameIn),str(addressIn),str(phNumberIn),str(genderIn),str(emailidIn),str(experIn),dt_string,empPicture)
                                                        # insert_query = "INSERT INTO student_registration(PID,first_name,last_name ,address ,phone_no,birthdate,gender,username ,passwd,email_id,class_id) VALUES('%s, %s, %s, %s, %s );" # queries for inserting values
                                                        print(args)
                                                        add_student = ("INSERT INTO studentDBMS.faculty"
                                                                        "(passwd,dept_id,qualification,birthdate,full_name,address, phone_no,gender,email_id, experience, login_date_time,profile_picture) "
                                                                        "VALUES (%s,%s,%s, %s,%s,%s ,%s,%s,%s, %s,%s,%s)")
                                                        cursor.execute(add_student,args) # executing the 
                                                        conn.commit() # commiting the connection then closing it.
                                                        conn.close() # closing the connection of the database
                                                        self.messagebox("Successful","Registration Successful,Wait For 5 seconds")
                                                        connagain = pymysql.connect(host, user=user,port=port,passwd=passwordDataBase, db=dbname)
                                                        print("connection successful for showing data")
                                                        cursor1=connagain.cursor()
                                                        argsAgain=(fullnameIn,emailidIn)
                                                        queryforemail="SELECT fac_id,passwd FROM studentDBMS.faculty where full_name=%s and email_id=%s;"
                                                        dets=cursor1.execute(queryforemail,argsAgain)
                                                        rec=cursor1.fetchall()
                                                        details=[rec[0][0],rec[0][1]]
                                                        self.sendEmailDetails(str(emailidIn),details)
                                                        cursor2=connagain.cursor()

                                                        connagain.commit()
                                                        connagain.close()
                                                        print("Details Sent Successfully")
                                                    else:
                                                        
                                                        self.warning("WRONG OTP","Incorrect OTP Entered")      
                                                    


                                            except pymysql.Error as error:
                                            
                                                self.warning("SQL ERROR",f"Failed inserting BLOB data into MySQL table {error}")
                                        else:
                                            self.warning("Department Error","Choose Correct Department")
                                    else:
                                        self.warning("Experience Error","Choose Correct Experience")
                                else:
                                    self.warning("Qulaification Error","Choose Correct Qualification")

                            else:
                                
                                self.warning("Password Error","Password Does Not Match")
                        else:
                            
                            self.warning("Incorrect Phone Number","Phone Number must be 10 Digits")
                    else:
                        
                        self.warning("Email ID Incorrect","Email Id Entered is Incorrect") 
                else:
                    
                    self.warning("Fullname Error! ","Incorrect Fullname")

            else:
                
                self.warning("Image Upload ERROR","Please Upload Your Image")
        else:
            
            self.warning("Incomplete","Please Enter All FIELDS")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminScreen = QtWidgets.QDialog()
    ui = Ui_AdminScreen("admin","admin")
    ui.setupUi(AdminScreen)
    AdminScreen.show()
    sys.exit(app.exec_())
