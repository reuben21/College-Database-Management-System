

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
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import images_rc
from requests import get
from AdminScreenMain import Ui_AdminScreen
from TeacherScreen import Ui_AdminScreen as teacherS
from StudentScreenMain import Ui_StudentScreen
try:
    host="localhost";user="root";dbname="studentDBMS"
    conn = pymysql.connect(host, user=user,port=3306,passwd="reuben", db=dbname)
    cursor=conn.cursor()
except Exception as e:
    print(e)


class Ui_DialogInformation(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 708)
        Dialog.setStyleSheet("background-color:#c5eff7;")
        Dialog.setWindowIcon(QtGui.QIcon('education.ico'))
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 731, 641))
        self.scrollArea.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 31))
        self.label.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 691, 131))
        self.textEdit.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:black;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 141, 31))
        self.label_2.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 230, 691, 131))
        self.textEdit_2.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:black;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 171, 31))
        self.label_3.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 410, 691, 211))
        self.textEdit_3.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:black;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.textEdit_3.setObjectName("textEdit_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.BackButtonInformation = QtWidgets.QPushButton(Dialog)
        self.BackButtonInformation.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.BackButtonInformation.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-login-rounded-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButtonInformation.setIcon(icon)
        self.BackButtonInformation.setIconSize(QtCore.QSize(30, 30))
        self.BackButtonInformation.setObjectName("BackButtonInformation")
        self.Inform = QtWidgets.QPushButton(Dialog)
        self.Inform.setGeometry(QtCore.QRect(240, 10, 221, 41))
        self.Inform.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inform.setIcon(icon1)
        self.Inform.setIconSize(QtCore.QSize(40, 40))
        self.Inform.setObjectName("Inform")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">ABOUT US:</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI Light\'; font-size:14pt; font-weight:24; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\"> College Database Management System </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Programmed in Python</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Using PyQT5 ,This is A GUI application</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">CREDITS:-</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Bruno Colas</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Berryl Coutinho</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Reuben Coutinho</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Dylan Coellho</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\">Simran Dhadich</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:10pt; font-weight:600; background-color:#ffffff;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">DEPARTMENTS:</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI Light\'; font-size:14pt; font-weight:24; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:11pt; font-weight:600; text-decoration: underline;\">INFORMATION TECHNOLOGY:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#000000; background-color:#ffffff;\">The progression of Information and Communication Technology is outpacing the expectations of humankind. Proliferation in the developments of Apps (Applications) and Robotics is astounding.we have total 120 seats available</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:600; color:#707070;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">COMPUTER ENGINEERING:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#000000; background-color:#ffffff;\">The undergraduate course in Computer Engineering started in 1999 with an intake of 60 seats which now has been reached up to 120 since 2010.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#000000; background-color:#ffffff;\">We have also started two postgraduate courses namely ME and Ph.D in Computer Engineering in year 2018 with the intake of 18 and 10 respectively.computer engineering consist of total 120 seats</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#707070;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">ELECTRICAL ENGINEERING:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#000000; background-color:#ffffff;\">The department encourages our students to develop new project ideas, which would be useful in the day to day life. They are also encouraged to undergo winter/summer internship in companies related to electrical stream. In a nutshell, the department is a motivation to the Electrical Engineering students in shaping up their destiny by keeping high aims of global competitive technocrats.Electrical engineering consist of total 120 seats</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#707070;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:600; text-decoration: underline; color:#000000; background-color:#ffffff;\">MECHANICAL ENGINEERING:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto,sans-serif\'; font-size:11pt; font-weight:400; color:#000000; background-color:#ffffff;\">In order to give them exposure to &quot;real word&quot;, we also have plans in place for industrial/field visits. Lectures, seminars and workshops by eminent personalities and industry experts in the field Mechanical Engineering are also being planned.Mechanical engineering consist of total 60 seats each year</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">LIST OF RECRUITERS</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI Light\'; font-size:14pt; font-weight:24; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">1.) TATA CONSULTANCY SERVICES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">2.) ACCENTURE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">3.) RELIANCE JIO INFOCOMM LIMITED</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">4.) L&amp;T INFOTECH</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">5.) TECH MAHINDRA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">6.) INFOSYS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">7.) HEXAWARE TECHNOLOGIES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">8.) ORACLE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">9.) ATOS CONSULTING &amp; TECHNOLOGY SERVICES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">10.) MACSOFT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">11.) VITAL HEALTH SOFTWARE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">12.) TPG CONSULTING SERVICES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">13.) INFORMATION ASSET</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">14.) NEOSOFT TECHNOLOGIES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">15.) FEEDSPOT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">16.) IBM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">17.) GODREJ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">18.) HCL TECHNOLOGIES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">19.) SIEMENS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400;\">20.) JUST DIAL.COM </span></p></body></html>"))
        self.BackButtonInformation.setText(_translate("Dialog", "BACK"))
        self.Inform.setText(_translate("Dialog", "INFORMATION"))




class Ui_DialogFeedBack(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(656, 608)
        Dialog.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color:#c5eff7;\n"
"")
        Dialog.setWindowIcon(QIcon('education.ico'))
        self.Department = QtWidgets.QComboBox(Dialog)
        self.Department.setGeometry(QtCore.QRect(230, 100, 201, 31))
        self.Department.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Department.setObjectName("Department")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(230, 150, 371, 31))
        self.comboBox.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.Punct_slider = QtWidgets.QSlider(Dialog)
        self.Punct_slider.setGeometry(QtCore.QRect(230, 280, 361, 22))
        self.Punct_slider.setStyleSheet("background-color:#c5eff7;")
        self.Punct_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Punct_slider.setObjectName("Punct_slider")
        self.class_hand_slider = QtWidgets.QSlider(Dialog)
        self.class_hand_slider.setGeometry(QtCore.QRect(230, 350, 361, 22))
        self.class_hand_slider.setStyleSheet("background-color:#c5eff7;")
        self.class_hand_slider.setOrientation(QtCore.Qt.Horizontal)
        self.class_hand_slider.setObjectName("class_hand_slider")
        self.Explain_Slider = QtWidgets.QSlider(Dialog)
        self.Explain_Slider.setGeometry(QtCore.QRect(230, 220, 361, 22))
        self.Explain_Slider.setStyleSheet("background-color:#c5eff7;")
        self.Explain_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Explain_Slider.setObjectName("Explain_Slider")

        self.DepartmentLabel = QtWidgets.QLabel(Dialog)
        self.DepartmentLabel.setGeometry(QtCore.QRect(40, 100, 161, 20))
        self.DepartmentLabel.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.DepartmentLabel.setObjectName("DepartmentLabel")


        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 111, 20))
        self.label_2.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 161, 20))
        self.label_4.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 171, 20))
        self.label_5.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 141, 31))
        self.label_6.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 530, 231, 51))
        self.pushButton.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.GetCourses = QtWidgets.QPushButton(Dialog)
        self.GetCourses.setGeometry(QtCore.QRect(450, 100, 130, 31))
        self.GetCourses.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.GetCourses.setObjectName("GetCourses")

        self.ExplainLabel = QtWidgets.QLabel(Dialog)
        self.ExplainLabel.setGeometry(QtCore.QRect(610, 220, 21, 16))
        self.ExplainLabel.setObjectName("ExplainLabel")
        self.Punct_Label = QtWidgets.QLabel(Dialog)
        self.Punct_Label.setGeometry(QtCore.QRect(610, 280, 21, 16))
        self.Punct_Label.setObjectName("Punct_Label")
        self.class_hand_Label = QtWidgets.QLabel(Dialog)
        self.class_hand_Label.setGeometry(QtCore.QRect(610, 350, 21, 16))
        self.class_hand_Label.setObjectName("class_hand_Label")
        self.Studentwelcome = QtWidgets.QPushButton(Dialog)
        self.Studentwelcome.setGeometry(QtCore.QRect(190, 30, 261, 41))
        self.Studentwelcome.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Studentwelcome.setIcon(icon)
        self.Studentwelcome.setIconSize(QtCore.QSize(40, 40))
        self.Studentwelcome.setObjectName("Studentwelcome")
        self.BackButtonFeedback = QtWidgets.QPushButton(Dialog)
        self.BackButtonFeedback.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.BackButtonFeedback.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-login-rounded-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButtonFeedback.setIcon(icon1)
        self.BackButtonFeedback.setIconSize(QtCore.QSize(30, 30))
        self.BackButtonFeedback.setObjectName("BackButtonFeedback")
        self.comments = QtWidgets.QTextEdit(Dialog)
        self.comments.setGeometry(QtCore.QRect(230, 420, 371, 71))
        self.comments.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"")
        self.comments.setObjectName("comments")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 420, 131, 20))
        self.label_7.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Punct_slider.setMinimum(0)
        self.Punct_slider.setMaximum(10)
        self.Punct_slider.setTickPosition(QSlider.TicksAbove) 
        self.Punct_slider.setTickInterval(1)
        self.Punct_slider.valueChanged.connect(self.getValue)
        self.class_hand_slider.setMinimum(0)
        self.class_hand_slider.setMaximum(10)
        self.class_hand_slider.setTickPosition(QSlider.TicksAbove) 
        self.class_hand_slider.setTickInterval(1)
        self.class_hand_slider.valueChanged.connect(self.getValue)
        self.Explain_Slider.setMinimum(0)
        self.Explain_Slider.setMaximum(10)
        self.Explain_Slider.setTickPosition(QSlider.TicksAbove) 
        self.Explain_Slider.setTickInterval(1)
        self.Explain_Slider.valueChanged.connect(self.getValue)
        self.pushButton.clicked.connect(self.Submit)
        self.GetCourses.clicked.connect(self.RefreshCoursesFunS)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p><a href=\"www.feedback.com\"><span style=\" text-decoration: underline; color:#0000ff;\">feedback</span></a></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p>COURSE ID:</p></body></html>"))
        self.DepartmentLabel.setText(_translate("Dialog", "<html><head/><body><p>DEPARTMENT:</p></body></html>"))
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT dept_id FROM studentdbms.department;"
        cursor.execute(query)
        result=cursor.fetchall()
        self.Department.addItem("")
        self.Department.setItemText(0, _translate("AdminScreen", "----Department----"))
        for i in range(1,len(result)):
                self.Department.addItem("")
                self.Department.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>PUNCTUALITY:</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>CLASS HANDLING:</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p>EXPLANATION:</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "SUBMIT FEEDBACK"))
        self.GetCourses.setText(_translate("Dialog", "GET COURSES"))
        self.ExplainLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.Punct_Label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.class_hand_Label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">0</p></body></html>"))
        self.Studentwelcome.setText(_translate("Dialog", "FeedBack Form"))
        self.BackButtonFeedback.setText(_translate("Dialog", "BACK"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p>COMMENTS:</p></body></html>"))
    def getValue(self):
        global punc_val,clas_hand,explaon
        punc_val=self.Punct_slider.value()
        clas_hand=self.class_hand_slider.value()
        explaon=self.Explain_Slider.value()
        
        self.class_hand_Label.setText(str(clas_hand))
        self.ExplainLabel.setText(str(explaon))
        self.Punct_Label.setText(str(punc_val))


    def Submit(self):
        global punc_val,clas_hand,explaon
        punc_val=self.Punct_slider.value()
        clas_hand=self.class_hand_slider.value()
        explaon=self.Explain_Slider.value()
        print(punc_val,clas_hand,explaon)

        course=self.comboBox.currentText()
        commentIn=self.comments.toPlainText()
        print(course,commentIn)
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        if course!="----Course----":
            if punc_val and clas_hand and explaon and commentIn:

                query = "INSERT INTO studentDBMS.feedback (course_id, explainantion, Punctuality, Class_Handling, Comments) VALUES (%s,%s,%s,%s,%s);"
                args=(course[0:6],explaon,punc_val,clas_hand,commentIn)
                cursor.execute(query,args)
                conn.commit()
                conn.close()
                self.messagebox("FeedBack Submitted","Thank You For Your Feedback")
            else:
                self.warning("Field Empty","Some Filed is Empty")
        else:
            self.warning("Select Course","Course Not Selected")        

    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('education.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('education.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def RefreshCoursesFunS(self):
        _translate = QtCore.QCoreApplication.translate
        deptId_T=self.Department.currentText()
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"

        print(deptId_T)
        if deptId_T!="----Department----" and deptId_T!="":
            try:
                self.comboBox.clear()
                conn = pymysql.connect(host, user=user,port=3306,passwd=password1, db=dbname)
                cursor=conn.cursor()
                query = "SELECT course_id,course_name from course where dept_id=%s;"
                cursor.execute(query,str(deptId_T))
                result=cursor.fetchall()
                print(result)
                if result!=():

                    listOfCourses=[None]
                    for i in range(len(result)):
                            listOfCourses.append(result[i][0]+"--"+result[i][1])
                    self.comboBox.addItem("")
                    self.comboBox.setItemText(0, _translate("AdminScreen", "----Course-ID----"))
                    for i in range(1,len(listOfCourses)):
                            self.comboBox.addItem("")
                            self.comboBox.setItemText(i, _translate("AdminScreen", f"{listOfCourses[i]}"))
                else:
                    self.comboBox.clear()
                    self.warning("No Courses","No Courses added in the department")

            except Exception as err:
                self.warning("SQL ERROR",f"{err}")
        else:
            self.warning("Wrong Department","Incorrect Department Selected")



class Ui_LoginScreen(object):
 
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
    def AdminScreen(self):
        adminuser=self.AdminPIDInput.text()
        adminpass=self.AdminPassInput.text()
        if adminuser:
            if adminpass:
                host="localhost";user="root";
                dbname="studentDBMS"
                conn = pymysql.connect(host, user=user,port=3306,passwd="reuben", db=dbname)
                cursor=conn.cursor()
                loginAdmin="SELECT * from administrator where Admin_Username=%s and Admin_Password=%s"
                dat=cursor.execute(loginAdmin,(adminuser,adminpass)) # executing the 
  
                if (len(cursor.fetchall())>0):
                    self.messagebox("Successful","You Have Successfully Logined")
                    self.adminwin=QtWidgets.QDialog()
                    self.ui=Ui_AdminScreen(adminuser,adminpass)
                    self.ui.setupUi(self.adminwin)
                    self.adminwin.show()
                else:
                    self.warning("Incorrect Details","Incorrect PID or Password")

                conn.commit() # commiting the connection then closing it.
                conn.close() # closing the connection of the database
            else:
                self.warning("Password Error","Password Not Entered")
        else:
            self.warning("Admin Error","Admin Username Not Entered")

    def TeacherScreen(self):
        adminuser=self.teacherIDinput.text()
        adminpass=self.TeacherPassInput.text()
        if adminuser:
            if adminpass:
                host="localhost";user="root";
                dbname="studentDBMS"
                conn = pymysql.connect(host, user=user,port=3306,passwd="reuben", db=dbname)
                cursor=conn.cursor()
                loginAdmin="SELECT * from faculty where fac_id=%s and passwd=%s"
                dat=cursor.execute(loginAdmin,(adminuser,adminpass)) # executing the 
          
                if (len(cursor.fetchall())>0):
                    self.messagebox("Successful","You Have Successfully Logined")
                    self.adminwin=QtWidgets.QDialog()
                    self.ui=teacherS(adminuser,adminpass)
                    self.ui.setupUi(self.adminwin)
                    self.adminwin.show()
                else:
                    self.warning("Incorrect Details","Incorrect PID or Password")

                conn.commit() # commiting the connection then closing it.
                conn.close() # closing the connection of the database
            else:
                self.warning("Password Error","Password Not Entered")
        else:
            self.warning("Admin Error","Admin Username Not Entered") 

    def loginfun(self):
        username=self.PIDstudent.text()
        password=self.PasswordStudent.text()
 
        if len(username)==6:
            if password:
                host="localhost";user="root";
                dbname="studentDBMS"
                conn = pymysql.connect(host, user=user,port=3306,passwd="reuben", db=dbname)
                cursor=conn.cursor()
                loginStudent="SELECT * from student_registration where PID=%s and passwd=%s"
                dat=cursor.execute(loginStudent,(username,password)) # executing the
                cursor2=conn.cursor()
                queryToApproval="SELECT Approval from student_registration where PID=%s and passwd=%s"
                cursor2.execute(queryToApproval,(username,password))
                Appro_Student=cursor2.fetchall()
                if (len(cursor.fetchall())>0):
                    if Appro_Student[0][0]!="NOT APPROVED":
                    
                        self.messagebox("Successful","You Have Successfully Logined")
                        self.adminwin=QtWidgets.QDialog()
                        self.ui=Ui_StudentScreen(username,password)
                        self.ui.setupUi(self.adminwin)
                        self.adminwin.show()
                    else:
                        self.warning("NOT APPROVED","YOUR DETAILS FOR APPROVAL ARE PENDING")
                        
                else:
                    self.warning("Incorrect Details","Incorrect PID or Password")

                conn.commit() # commiting the connection then closing it.
                conn.close() # closing the connection of the database
            else:
                self.warning("Password","Password Not Entered")
        else:
            self.warning("Incorrect PID","PID is A 6-digit Number")
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(801, 611)
        LoginScreen.setStyleSheet("background-color:#c5eff7;")
        LoginScreen.setWindowTitle("Login Screen")
        LoginScreen.setWindowIcon(QIcon('education.ico'))
        self.login_Screens = QtWidgets.QTabWidget(LoginScreen)
        self.login_Screens.setGeometry(QtCore.QRect(130, 120, 571, 401))
        self.login_Screens.setStyleSheet("color:#1e8bc3;\n""border-radius: 10px;\n""border:1px solid #c5eff7;\n""")
        self.login_Screens.setTabPosition(QtWidgets.QTabWidget.North)
        self.login_Screens.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.login_Screens.setIconSize(QtCore.QSize(30, 30))
        self.login_Screens.setElideMode(QtCore.Qt.ElideLeft)
        self.login_Screens.setObjectName("login_Screens")
        self.StudentLogin = QtWidgets.QWidget()
        self.StudentLogin.setObjectName("StudentLogin")
        self.studentPIDlabel = QtWidgets.QLabel(self.StudentLogin)
        self.studentPIDlabel.setGeometry(QtCore.QRect(80, 80, 81, 31))
        self.studentPIDlabel.setObjectName("studentPIDlabel")
        self.PIDstudent = QtWidgets.QLineEdit(self.StudentLogin)
        self.PIDstudent.setGeometry(QtCore.QRect(230, 80, 151, 41))
        self.PIDstudent.setStyleSheet("background-color:white;\n""border-radius:10px;\n""border: 1px solid #1e8bc3;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.PIDstudent.setObjectName("PIDstudent")
        self.studentPasswordlabel = QtWidgets.QLabel(self.StudentLogin)
        self.studentPasswordlabel.setGeometry(QtCore.QRect(80, 160, 111, 31))
        self.studentPasswordlabel.setObjectName("studentPasswordlabel")
        self.PasswordStudent = QtWidgets.QLineEdit(self.StudentLogin)
        self.PasswordStudent.setGeometry(QtCore.QRect(230, 160, 151, 41))
        self.PasswordStudent.setStyleSheet("background-color:white;\n""border-radius:10px;\n""border: 1px solid #1e8bc3;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.PasswordStudent.setObjectName("PasswordStudent")
        self.PasswordStudent.setEchoMode(QtWidgets.QLineEdit.Password)
        self.StudentBtn = QtWidgets.QPushButton(self.StudentLogin)
        self.StudentBtn.setGeometry(QtCore.QRect(250, 250, 121, 41))
        self.StudentBtn.setStyleSheet("background-color:#1e8bc3;\n""border-radius: 10px;\n""color:white;\n""font: 25 20pt \"Microsoft YaHei UI Light\";\n""border:3px solid white;\n""")
        self.StudentBtn.setObjectName("StudentBtn")
        self.StudentBtn.clicked.connect(self.loginfun)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_Screens.addTab(self.StudentLogin, icon, "")
        self.TeacherLogin = QtWidgets.QWidget()
        self.TeacherLogin.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TeacherLogin.setObjectName("TeacherLogin")
        self.teacherIDinput = QtWidgets.QLineEdit(self.TeacherLogin)
        self.teacherIDinput.setGeometry(QtCore.QRect(240, 80, 151, 41))
        self.teacherIDinput.setStyleSheet("background-color:white;\n""border-radius:10px;\n""border: 1px solid #1e8bc3;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.teacherIDinput.setObjectName("teacherIDinput")
        self.TeacherPassInput = QtWidgets.QLineEdit(self.TeacherLogin)
        self.TeacherPassInput.setGeometry(QtCore.QRect(240, 160, 151, 41))
        self.TeacherPassInput.setStyleSheet("background-color:white;\n""border-radius:10px;\n""border: 1px solid #1e8bc3;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.TeacherPassInput.setObjectName("TeacherPassInput")
        self.TeacherPassInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.FacultyPasswordlabel_2 = QtWidgets.QLabel(self.TeacherLogin)
        self.FacultyPasswordlabel_2.setGeometry(QtCore.QRect(90, 160, 111, 31))
        self.FacultyPasswordlabel_2.setObjectName("FacultyPasswordlabel_2")
        self.FacultyPIDlabel_2 = QtWidgets.QLabel(self.TeacherLogin)
        self.FacultyPIDlabel_2.setGeometry(QtCore.QRect(90, 80, 111, 31))
        self.FacultyPIDlabel_2.setObjectName("FacultyPIDlabel_2")
        self.TeacherLoginBtn = QtWidgets.QPushButton(self.TeacherLogin)
        self.TeacherLoginBtn.setGeometry(QtCore.QRect(250, 250, 121, 41))
        self.TeacherLoginBtn.setStyleSheet("background-color:#1e8bc3;\n""border-radius: 10px;\n""color:white;\n""font: 25 20pt \"Microsoft YaHei UI Light\";\n""border:3px solid white;\n""")
        self.TeacherLoginBtn.setObjectName("TeacherLoginBtn")
        self.TeacherLoginBtn.clicked.connect(self.TeacherScreen)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-teacher-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_Screens.addTab(self.TeacherLogin, icon1, "")
        self.Admin_Login = QtWidgets.QWidget()
        self.Admin_Login.setObjectName("Admin_Login")
        self.AdminPIDInput = QtWidgets.QLineEdit(self.Admin_Login)
        self.AdminPIDInput.setGeometry(QtCore.QRect(250, 80, 151, 41))
        self.AdminPIDInput.setStyleSheet("background-color:white;\n""border-radius:10px;\n""border: 1px solid #1e8bc3;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.AdminPIDInput.setObjectName("AdminPIDInput")
        self.AdminPassInput = QtWidgets.QLineEdit(self.Admin_Login)
        self.AdminPassInput.setGeometry(QtCore.QRect(250, 160, 151, 41))
        self.AdminPassInput.setStyleSheet("background-color:white;\n""border-radius:10px;\n""border: 1px solid #1e8bc3;\n""font: 14pt \"MS Shell Dlg 2\";")
        self.AdminPassInput.setObjectName("AdminPassInput")
        self.AdminPassInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.studentPasswordlabel_3 = QtWidgets.QLabel(self.Admin_Login)
        self.studentPasswordlabel_3.setGeometry(QtCore.QRect(100, 160, 111, 31))
        self.studentPasswordlabel_3.setObjectName("studentPasswordlabel_3")
        self.studentPIDlabel_3 = QtWidgets.QLabel(self.Admin_Login)
        self.studentPIDlabel_3.setGeometry(QtCore.QRect(100, 80, 101, 31))
        self.studentPIDlabel_3.setObjectName("studentPIDlabel_3")
        self.AdimLoginBtn = QtWidgets.QPushButton(self.Admin_Login)
        self.AdimLoginBtn.setGeometry(QtCore.QRect(260, 250, 121, 41))
        self.AdimLoginBtn.setStyleSheet("background-color:#1e8bc3;\n""border-radius: 10px;\n""color:white;\n""font: 25 20pt \"Microsoft YaHei UI Light\";\n""border:3px solid white;\n""")
        self.AdimLoginBtn.setObjectName("AdimLoginBtn")
        self.AdimLoginBtn.clicked.connect(self.AdminScreen)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-microsoft-admin-90.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_Screens.addTab(self.Admin_Login, icon2, "")
        self.pushButton_2 = QtWidgets.QPushButton(LoginScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 20, 221, 51))
        self.pushButton_2.setStyleSheet("border: 1px solid #1e8bc3;\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/multiple-users-silhouette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.BackButton = QtWidgets.QPushButton(LoginScreen)
        self.BackButton.setGeometry(QtCore.QRect(40, 30, 81, 31))
        self.BackButton.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-login-rounded-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon4)
        self.BackButton.setIconSize(QtCore.QSize(30, 30))
        self.BackButton.setObjectName("BackButton")
        self.retranslateUi(LoginScreen)
        self.login_Screens.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Login Screen"))
        self.studentPIDlabel.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">PID:</span></p></body></html>"))
        self.studentPasswordlabel.setText(_translate("LoginScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.StudentBtn.setText(_translate("LoginScreen", "Login"))
        self.login_Screens.setTabText(self.login_Screens.indexOf(self.StudentLogin), _translate("LoginScreen", "Student Login"))
        self.FacultyPasswordlabel_2.setText(_translate("LoginScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.FacultyPIDlabel_2.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Faculty ID:</span></p></body></html>"))
        self.TeacherLoginBtn.setText(_translate("LoginScreen", "Login"))
        self.login_Screens.setTabText(self.login_Screens.indexOf(self.TeacherLogin), _translate("LoginScreen", "Teacher Login"))
        self.studentPasswordlabel_3.setText(_translate("LoginScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.studentPIDlabel_3.setText(_translate("LoginScreen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Admin ID:</span></p></body></html>"))
        self.AdimLoginBtn.setText(_translate("LoginScreen", "Login"))
        self.login_Screens.setTabText(self.login_Screens.indexOf(self.Admin_Login), _translate("LoginScreen", "Admin Login"))
        self.pushButton_2.setText(_translate("LoginScreen", "LOGIN SCREEN"))
        self.BackButton.setText(_translate("LoginScreen", "BACK"))

class Ui_Registration_Page(object):
       
    def convertToBinaryData(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def sendEmailOtp(self,receiver_email,otp):
        sender_email = "student.sdbms@gmail.com"
         
        password = "Reuben@21"

        message = MIMEMultipart("alternative")
        message["Subject"] = "One-Time Password Verification"
        message["From"] = sender_email
        message["To"] = receiver_email


        html = f"""\
        <html>
          <body>
            <p><h3>Hello,Thank your for Registering with us.</h3><br>
              <h1>Your One-Time Password is: {otp}</h1> 
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects

        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first

        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465 , context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )       
    
    def sendEmailDetails(self,receiver_email,otp):


        sender_email = "student.sdbms@gmail.com"
         
        password = "Reuben@21"

        message = MIMEMultipart("alternative")
        message["Subject"] = "One-Time Password Verification"
        message["From"] = sender_email
        message["To"] = receiver_email
        html = f"""\
        <html>
          <body>
            <p><h3>Hello,Thank your for Registering with us.</h3><br>
              <h1>Login Details: \n PID:- {otp[0]} \n Password:- {otp[1]}</h1> 
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects

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
    def setupUi(self, Registration_Page):
        Registration_Page.setObjectName("Registration_Page")
        Registration_Page.resize(805, 642)
        Registration_Page.setStyleSheet("background-color:#c5eff7;")
        Registration_Page.setWindowTitle("Student Registration Page")
        Registration_Page.setWindowIcon(QIcon('education.ico'))
        self.MALE = QtWidgets.QRadioButton(Registration_Page)
        self.MALE.setGeometry(QtCore.QRect(310, 310, 51, 17))
        self.MALE.setStyleSheet("color:#1e8bc3;")
        self.MALE.setObjectName("MALE")
        self.MALE.setChecked(True)
        self.FEMALE = QtWidgets.QRadioButton(Registration_Page)
        self.FEMALE.setGeometry(QtCore.QRect(370, 310, 61, 17))
        self.FEMALE.setStyleSheet("color:#1e8bc3;")
        self.FEMALE.setObjectName("FEMALE")
        self.OTHERS = QtWidgets.QRadioButton(Registration_Page)
        self.OTHERS.setGeometry(QtCore.QRect(440, 310, 61, 17))
        self.OTHERS.setStyleSheet("color:#1e8bc3;")
        self.OTHERS.setObjectName("OTHERS")
        self.Submit = QtWidgets.QPushButton(Registration_Page)
        self.Submit.setGeometry(QtCore.QRect(310, 590, 181, 41))
        self.Submit.setMouseTracking(True)
        self.Submit.setTabletTracking(True)
 
        self.Submit.setAutoFillBackground(False)
        self.Submit.setStyleSheet("background-color:#1e8bc3;\n""border-radius: 10px;\n""color:white;\n""font: 25 20pt \"Microsoft YaHei UI Light\";\n""border:3px solid white;\n""")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/submit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Submit.setIcon(icon)
        self.Submit.setIconSize(QtCore.QSize(30, 30))
        self.Submit.setObjectName("Submit")
        self.Submit.clicked.connect(self.SubmitDetails)
        self.UploadPicture = QtWidgets.QPushButton(Registration_Page)
        self.UploadPicture.setGeometry(QtCore.QRect(570, 280, 151, 41))
        self.UploadPicture.setStyleSheet("background-color:#1e8bc3;\n""border-radius: 10px;\n""color:white;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""border:3px solid white;\n""")
        self.UploadPicture.setObjectName("UploadPicture")
        self.UploadPicture.clicked.connect(self.openImage)
        self.ImageLabel = QtWidgets.QLabel(Registration_Page)
        self.ImageLabel.setGeometry(QtCore.QRect(590, 110, 111, 151))
        self.ImageLabel.setStyleSheet("background-color:#1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""border-radius: 10px;\n""color:white;")
        self.ImageLabel.setText("")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.ReturnLogin = QtWidgets.QPushButton(Registration_Page)
        self.ReturnLogin.setGeometry(QtCore.QRect(600, 10, 201, 31))
        self.ReturnLogin.setStyleSheet("color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";\n""border: 1px solid #1e8bc3;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReturnLogin.setIcon(icon1)
        self.ReturnLogin.setIconSize(QtCore.QSize(25, 25))
        self.ReturnLogin.setObjectName("ReturnLogin")
        self.BackButton = QtWidgets.QPushButton(Registration_Page)
        self.BackButton.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.BackButton.setStyleSheet("border: 1px solid #1e8bc3;\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-login-rounded-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon2)
        self.BackButton.setIconSize(QtCore.QSize(30, 30))
        self.BackButton.setObjectName("BackButton")
        self.pushButton = QtWidgets.QPushButton(Registration_Page)
        self.pushButton.setGeometry(QtCore.QRect(210, 20, 351, 51))
        self.pushButton.setStyleSheet("border: 1px solid #1e8bc3;\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.re_passwordlabel = QtWidgets.QLabel(Registration_Page)
        self.re_passwordlabel.setGeometry(QtCore.QRect(130, 510, 156, 19))
        self.re_passwordlabel.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.re_passwordlabel.setObjectName("re_passwordlabel")
        self.fullname = QtWidgets.QLineEdit(Registration_Page)
        self.fullname.setGeometry(QtCore.QRect(300, 110, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullname.sizePolicy().hasHeightForWidth())
        self.fullname.setSizePolicy(sizePolicy)
        self.fullname.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.fullname.setObjectName("fullname")
        self.dateofbirth = QtWidgets.QDateEdit(Registration_Page)
        self.dateofbirth.setGeometry(QtCore.QRect(300, 260, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.dateofbirth.setFont(font)
        self.dateofbirth.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateofbirth.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dateofbirth.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.dateofbirth.setWrapping(True)
        self.dateofbirth.setAlignment(QtCore.Qt.AlignCenter)
        self.dateofbirth.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateofbirth.setAccelerated(True)
        self.dateofbirth.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateofbirth.setProperty("showGroupSeparator", True)
        self.dateofbirth.setObjectName("dateofbirth")
        self.full_name = QtWidgets.QLabel(Registration_Page)
        self.full_name.setGeometry(QtCore.QRect(130, 110, 81, 19))
        self.full_name.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name.setObjectName("full_name")
        self.email_id_2 = QtWidgets.QLabel(Registration_Page)
        self.email_id_2.setGeometry(QtCore.QRect(130, 360, 71, 19))
        self.email_id_2.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.email_id_2.setObjectName("email_id_2")
        self.phone_number_2 = QtWidgets.QLabel(Registration_Page)
        self.phone_number_2.setGeometry(QtCore.QRect(130, 400, 120, 19))
        self.phone_number_2.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.phone_number_2.setObjectName("phone_number_2")
        self.dept = QtWidgets.QComboBox(Registration_Page)
        self.dept.setGeometry(QtCore.QRect(300, 550, 191, 31))
        self.dept.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.dept.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.dept.setObjectName("dept")
        self.email_id = QtWidgets.QLineEdit(Registration_Page)
        self.email_id.setGeometry(QtCore.QRect(300, 350, 191, 31))
        self.email_id.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.email_id.setObjectName("email_id")
        self.password_2 = QtWidgets.QLabel(Registration_Page)
        self.password_2.setGeometry(QtCore.QRect(130, 450, 78, 19))
        self.password_2.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.password_2.setObjectName("password_2")
        self.re_password = QtWidgets.QLineEdit(Registration_Page)
        self.re_password.setGeometry(QtCore.QRect(300, 500, 191, 31))
        self.re_password.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.re_password.setObjectName("re_password")
        self.re_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gender = QtWidgets.QLabel(Registration_Page)
        self.gender.setGeometry(QtCore.QRect(130, 310, 59, 19))
        self.gender.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.gender.setObjectName("gender")
        self.dateofbirth_2 = QtWidgets.QLabel(Registration_Page)
        self.dateofbirth_2.setGeometry(QtCore.QRect(130, 270, 107, 19))
        self.dateofbirth_2.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirth_2.setObjectName("dateofbirth_2")
        self.password = QtWidgets.QLineEdit(Registration_Page)
        self.password.setGeometry(QtCore.QRect(300, 450, 191, 31))
        self.password.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.address = QtWidgets.QLabel(Registration_Page)
        self.address.setGeometry(QtCore.QRect(130, 170, 65, 19))
        self.address.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.address.setObjectName("address")
        self.phone_number = QtWidgets.QLineEdit(Registration_Page)
        self.phone_number.setGeometry(QtCore.QRect(300, 400, 191, 31))
        self.phone_number.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.phone_number.setObjectName("phone_number")
        self.label_9 = QtWidgets.QLabel(Registration_Page)
        self.label_9.setGeometry(QtCore.QRect(130, 550, 98, 19))
        self.label_9.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.Address = QtWidgets.QTextEdit(Registration_Page)
        self.Address.setGeometry(QtCore.QRect(300, 160, 191, 81))
        self.Address.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 12pt \"Microsoft YaHei UI Light\";\n""")
        self.Address.setObjectName("Address")

        self.retranslateUi(Registration_Page)
        QtCore.QMetaObject.connectSlotsByName(Registration_Page)
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
        fullnameIn=self.fullname.text()
        passwordIn=self.password.text()
        repasswordIn=self.re_password.text()
        addressIn=self.Address.toPlainText()
        dobIn=self.dateofbirth.date().toPyDate()
        phNumberIn=self.phone_number.text()
        emailidIn=self.email_id.text()
        
        if self.MALE.isChecked():
            genderIn="Male"
        elif self.FEMALE.isChecked():
            genderIn="Female"
        elif self.OTHERS.isChecked():
            genderIn="Others"
        deptIn=self.dept.currentText()
        print(fullnameIn,passwordIn,repasswordIn,addressIn,dobIn,phNumberIn,emailidIn,genderIn,deptIn)
        digits = "0123456789"
        OTP = "" 
      

        for i in range(6) : 
            OTP += digits[math.floor(random.random() * 10)]         
        otp=OTP
        print(otp)

        host="localhost";user="root";password1="reuben";dbname="studentDBMS"
        conn = pymysql.connect(host, user=user,port=3306,passwd=password1, db=dbname)
        cursor=conn.cursor()
        cursor.execute("Truncate onetime")
        query=("INSERT into onetime""(numbers)""VALUES (%s)")
        c=cursor.execute(query,otp)
        query12="SELECT * FROM studentDBMS.onetime"
        cursor.execute(query12)

        records = cursor.fetchall()
   
        listtemp=[]
        for record in records:
            listtemp.append(int(record[1]))
        
        

        

        wp = "NOT APPROVED"
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")

        
        pass

        if fullnameIn and addressIn and emailidIn and phNumberIn and repasswordIn and passwordIn and genderIn and dobIn and deptIn:
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
                                if "a"=="a":
                                    pass                                    
                                    try:
                                        # host="reubendbms.csubdeug2c1q.ap-south-1.rds.amazonaws.com"
                                        # port=3347
                                        # dbname="studentDBMS"
                                        # user="root"
                                        # password2="reuben21"
                                        empPicture = self.convertToBinaryData(strimg)
                                        self.sendEmailOtp(str(emailidIn),otp)
        

                                        i, okPressed = QInputDialog.getInt(None,"Get integer",f"Enter the OTP sent to Email-ID:{emailidIn}", 1, -2147483647, 2147483647, 1)
                                        if okPressed:
                                            print(i) 
                                            if int(i) in listtemp:
                                                print("Email Verified Successfully")

                                                conn = pymysql.connect(host, user=user,port=3306,passwd=password1, db=dbname)
                                                print("connection successful")
                                                cursor=conn.cursor()
                                                args=(str(fullnameIn),str(addressIn),str(phNumberIn),dobIn,str(genderIn),str(passwordIn),str(emailidIn),str(deptIn),dt_string,str(wp),empPicture)
                                                # insert_query = "INSERT INTO student_registration(PID,first_name,last_name ,address ,phone_no,birthdate,gender,username ,passwd,email_id,class_id) VALUES('%s, %s, %s, %s, %s );" # queries for inserting values
                                                add_student = ("INSERT INTO student_registration "
                                                                "(full_name,address, phone_no,birthdate,gender, passwd,email_id,id_dept, last_login_time_date,Approval,profile_picture) "
                                                                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                                                cursor.execute(add_student,args) # executing the 
                                                conn.commit() # commiting the connection then closing it.
                                                conn.close() # closing the connection of the database
                                                self.messagebox("Successful","Registration Successful,Wait For 5 seconds")
                                                connagain = pymysql.connect(host, user=user,port=3306,passwd=password1, db=dbname)
                                                print("connection successful for showing data")
                                                cursor1=connagain.cursor()
                                                queryforemail="SELECT PID,passwd FROM studentDBMS.student_registration where full_name=%s;"
                                                dets=cursor1.execute(queryforemail,fullnameIn)
                                                rec=cursor1.fetchall()
                                                details=[rec[0][0],rec[0][1]]
                                                self.sendEmailDetails(str(emailidIn),details)

                                                connagain.commit()
                                                connagain.close()
                                                print("Details Sent Successfully")
                                                print("Image Sent Successfully")

                                            else:
                                                
                                                self.warning("WRONG OTP","Incorrect OTP Entered")
                                        else:
                                            self.warning("Incorrect OTP","Incorrect OTP")                                             


                                    except pymysql.Error as error:
                                        
                                        self.warning("SQL ERROR",f"Failed inserting BLOB data into MySQL table {error}")

                            else:
                                
                                self.warning("Password Error","Password Does Not Match")
                        else:
                            
                            self.warning("Incorrect Phone Number","Phone Number must be 10 Digits")
                    else:
                        
                        self.warning("Email ID Incorrect","Email Id Entered is Incorrect") 
                else:
                    
                    self.warning("Fullname Error! ","Incorrect Fullname")

            else:
                
                self.warning("Image ERROR","Upload Image")
        else:
            
            self.warning("Incomplete","Please Enter All FIELDS")
    def generateOTP(self) : 
      
        # Declare a digits variable   
        # which stores all digits  
        digits = "0123456789"
        OTP = "" 
      
       # length of password can be chaged 
       # by changing value in range 
        for i in range(6) : 
            OTP += digits[math.floor(random.random() * 10)] 
      
        return OTP 
    def retranslateUi(self, Registration_Page):
        _translate = QtCore.QCoreApplication.translate
        Registration_Page.setWindowTitle(_translate("Registration_Page", "Student Registration Page"))
        self.MALE.setText(_translate("Registration_Page", "MALE"))
        self.FEMALE.setText(_translate("Registration_Page", "FEMALE"))
        self.OTHERS.setText(_translate("Registration_Page", "OTHERS"))
        self.Submit.setText(_translate("Registration_Page", "SUBMIT"))
        self.UploadPicture.setText(_translate("Registration_Page", "Upload Picture"))
        self.ReturnLogin.setText(_translate("Registration_Page", "TO LOGIN SCREEN"))
        self.BackButton.setText(_translate("Registration_Page", "BACK"))
        self.pushButton.setText(_translate("Registration_Page", "STUDENT REGISTRATION FORM"))
        self.re_passwordlabel.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Re-Enter Password</span></p></body></html>"))
        self.full_name.setToolTip(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.email_id_2.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Email-ID</span></p></body></html>"))
        self.phone_number_2.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT dept_id FROM studentdbms.department;"
        cursor.execute(query)
        result=cursor.fetchall()
        self.dept.addItem("")
        self.dept.setItemText(0, _translate("Registration_Page", "----Department----"))
        for i in range(1,len(result)):
                self.dept.addItem("")
                self.dept.setItemText(i, _translate("Registration_Page", f"{result[i][0]}"))
        self.password_2.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.gender.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Gender</span></p></body></html>"))
        self.dateofbirth_2.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Date Of Birth</span></p></body></html>"))
        self.address.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Address</span></p></body></html>"))
        self.label_9.setText(_translate("Registration_Page", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Department</span></p></body></html>"))



class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("Main Screen")
        MainScreen.setWindowIcon(QIcon('education.ico'))
        MainScreen.resize(801, 604)
        MainScreen.setWindowOpacity(1.0)
        MainScreen.setStyleSheet("background-color:#c5eff7;\n"
"background-image:url(:/newPrefix/home.png)")
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.RegisterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterBtn.setGeometry(QtCore.QRect(70, 420, 301, 81))
        self.RegisterBtn.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border: 1px solid #1e8bc3;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RegisterBtn.setIcon(icon)
        self.RegisterBtn.setIconSize(QtCore.QSize(80, 80))
        self.RegisterBtn.setObjectName("RegisterBtn")
        self.InformationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.InformationBtn.setGeometry(QtCore.QRect(440, 420, 301, 81))
        self.InformationBtn.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border: 1px solid #1e8bc3;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.InformationBtn.setIcon(icon1)
        self.InformationBtn.setIconSize(QtCore.QSize(80, 80))
        self.InformationBtn.setObjectName("InformationBtn")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(70, 270, 301, 81))
        self.LoginBtn.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border: 1px solid #1e8bc3;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoginBtn.setIcon(icon2)
        self.LoginBtn.setIconSize(QtCore.QSize(80, 80))
        self.LoginBtn.setCheckable(False)
        self.LoginBtn.setObjectName("LoginBtn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 270, 301, 81))
        self.pushButton.setStyleSheet("background: transparent;\n"
"border-radius: 15px;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"border: 1px solid #1e8bc3;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/feedback.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 331, 201))
        self.label.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"background:transparent;\n"
"")
        self.label.setObjectName("label")
        MainScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("Main Screen", "Main Screen"))
        self.RegisterBtn.setText(_translate("MainScreen", "Student Registration"))
        self.InformationBtn.setText(_translate("MainScreen", "Information"))
        self.LoginBtn.setText(_translate("MainScreen", "LOGIN"))
        self.pushButton.setText(_translate("MainScreen", "Feedback"))
        self.label.setText(_translate("MainScreen", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/icons8-student-center-100 (1).png\"/></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">COLLEGE DATABASE </span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">MANAGEMENT SYSTEM</span></p></body></html>"))


class DialogUi_LoginScreen(QtWidgets.QDialog, Ui_LoginScreen):
    def __init__(self, parent=None):
        super(DialogUi_LoginScreen, self).__init__(parent)
        self.setupUi(self)
        # close the window
        self.BackButton.clicked.connect(self.close)
    # def BackToRegister(self):
    #     self.window=QtWidgets.QMainWindow()
    #     self.ui1=Ui_MainScreen()
    #     self.ui1.setupUi2(self.window)
    #     self.hide()
    #     self.window.show()     
class DialogUi_Registration_Page(QtWidgets.QDialog, Ui_Registration_Page):
    def __init__(self, parent=None):
        super(DialogUi_Registration_Page, self).__init__(parent)
        self.setupUi(self)
        # close the window
        self.BackButton.clicked.connect(self.close)
        self.ReturnLogin.clicked.connect(self.close)


class DialogMainUi_MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):
    def __init__(self, parent=None):
        super(DialogMainUi_MainScreen, self).__init__(parent)
        self.setupUi(self)
        # close the window
        self.LoginBtn.clicked.connect(self.close)
        self.RegisterBtn.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.close)
        self.InformationBtn.clicked.connect(self.close)
         
class DialogUi_DialogFeedback(QtWidgets.QDialog, Ui_DialogFeedBack):
    def __init__(self, parent=None):
        super(DialogUi_DialogFeedback, self).__init__(parent)
        self.setupUi(self)
        # close the window
        
        self.BackButtonFeedback.clicked.connect(self.close)
class DialogUi_DialogInformation(QtWidgets.QDialog, Ui_DialogInformation):
    def __init__(self, parent=None):
        super(DialogUi_DialogInformation, self).__init__(parent)
        self.setupUi(self)
        # close the window
        
        self.BackButtonInformation.clicked.connect(self.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QPixmap(":/newPrefix/splashSreenFinal.png")

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    progressBar = QProgressBar(splash)
    progressBar.setMaximum(10)
    progressBar.setGeometry(75, splash_pix.height() - 50, 900, 20)

    # splash.setMask(splash_pix.mask())

    splash.show()

    
    for i in range(1, 12):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
           app.processEvents()

    # Simulate something that takes time
    time.sleep(1)

    w1=DialogUi_LoginScreen()
    w2=DialogUi_Registration_Page()
    feedback=DialogUi_DialogFeedback()
    info=DialogUi_DialogInformation()
    MainScreen = DialogMainUi_MainScreen()
    splash.finish(MainScreen)
    
    MainScreen.RegisterBtn.clicked.connect(w2.show)
    MainScreen.LoginBtn.clicked.connect(w1.show)
    MainScreen.pushButton.clicked.connect(feedback.show)
    MainScreen.InformationBtn.clicked.connect(info.show)
    w1.BackButton.clicked.connect(MainScreen.show)
    w2.BackButton.clicked.connect(MainScreen.show)
    w2.ReturnLogin.clicked.connect(w1.show)
    feedback.BackButtonFeedback.clicked.connect(MainScreen.show)
    info.BackButtonInformation.clicked.connect(MainScreen.show)
    MainScreen.show()
    
    sys.exit(app.exec_())






