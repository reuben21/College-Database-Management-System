


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
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import images_rc
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

import time

class Ui_StudentScreen(object):
    def __init__(self,S_PID,S_pass):
        self.Student_PID=S_PID
        self.Student_pass=S_pass
        host="localhost";port=3306;dbname="studentDBMS";user="root";password1="reuben"
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        cursor=conn.cursor()
        query="SELECT * FROM studentDBMS.student_registration WHERE PID=%s and Passwd=%s"
        args=(self.Student_PID,self.Student_pass)
        cursor.execute(query,args)
        records=cursor.fetchall()
        print(records)
        self.Student_Name=records[0][1]
        conn.commit()
        conn.close()
    def setupUi(self, StudentScreen):
        StudentScreen.setObjectName("StudentScreen")
        StudentScreen.resize(1132, 670)
        StudentScreen.setStyleSheet("background-color:#c5eff7;")
        StudentScreen.setWindowIcon(QIcon('education.ico'))
        self.Studentwelcome = QtWidgets.QPushButton(StudentScreen)
        self.Studentwelcome.setGeometry(QtCore.QRect(290, 20, 491, 61))
        self.Studentwelcome.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/StudentHeader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Studentwelcome.setIcon(icon)
        self.Studentwelcome.setIconSize(QtCore.QSize(50, 50))
        self.Studentwelcome.setObjectName("Studentwelcome")
        self.tabWidget = QtWidgets.QTabWidget(StudentScreen)
        self.tabWidget.setGeometry(QtCore.QRect(20, 120, 1091, 531))
        self.tabWidget.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 10px;\n"
"border:1px solid #c5eff7;\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setObjectName("tabWidget")
        self.Update_details = QtWidgets.QWidget()
        self.Update_details.setObjectName("Update_details")
        self.full_name = QtWidgets.QLabel(self.Update_details)
        self.full_name.setGeometry(QtCore.QRect(20, 30, 91, 19))
        self.full_name.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name.setObjectName("full_name")
        self.fullnameLine = QtWidgets.QLineEdit(self.Update_details)
        self.fullnameLine.setGeometry(QtCore.QRect(143, 34, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullnameLine.sizePolicy().hasHeightForWidth())
        self.fullnameLine.setSizePolicy(sizePolicy)
        self.fullnameLine.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.fullnameLine.setObjectName("fullnameLine")
        self.address = QtWidgets.QLabel(self.Update_details)
        self.address.setGeometry(QtCore.QRect(530, 110, 71, 20))
        self.address.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.address.setObjectName("address")
        self.AddressLine = QtWidgets.QTextEdit(self.Update_details)
        self.AddressLine.setGeometry(QtCore.QRect(630, 90, 241, 91))
        self.AddressLine.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"")
        self.AddressLine.setObjectName("AddressLine")
        self.gender = QtWidgets.QLabel(self.Update_details)
        self.gender.setGeometry(QtCore.QRect(20, 100, 71, 19))
        self.gender.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.gender.setObjectName("gender")
        self.GenderLine = QtWidgets.QLineEdit(self.Update_details)
        self.GenderLine.setGeometry(QtCore.QRect(143, 94, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GenderLine.sizePolicy().hasHeightForWidth())
        self.GenderLine.setSizePolicy(sizePolicy)
        self.GenderLine.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.GenderLine.setObjectName("GenderLine")
        self.password = QtWidgets.QLineEdit(self.Update_details)
        self.password.setGeometry(QtCore.QRect(630, 200, 241, 31))
        self.password.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.password.setObjectName("password")
        self.password_2 = QtWidgets.QLabel(self.Update_details)
        self.password_2.setGeometry(QtCore.QRect(520, 200, 91, 20))
        self.password_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.password_2.setObjectName("password_2")
        self.phone_numberline = QtWidgets.QLineEdit(self.Update_details)
        self.phone_numberline.setGeometry(QtCore.QRect(143, 154, 191, 31))
        self.phone_numberline.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.phone_numberline.setObjectName("phone_numberline")
        self.phone_number_2 = QtWidgets.QLabel(self.Update_details)
        self.phone_number_2.setGeometry(QtCore.QRect(10, 160, 131, 21))
        self.phone_number_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.phone_number_2.setObjectName("phone_number_2")
        self.email_idline = QtWidgets.QLineEdit(self.Update_details)
        self.email_idline.setGeometry(QtCore.QRect(140, 210, 351, 31))
        self.email_idline.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.email_idline.setText("")
        self.email_idline.setObjectName("email_idline")
        self.email_id_2 = QtWidgets.QLabel(self.Update_details)
        self.email_id_2.setGeometry(QtCore.QRect(13, 214, 91, 20))
        self.email_id_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.email_id_2.setObjectName("email_id_2")
        self.label_9 = QtWidgets.QLabel(self.Update_details)
        self.label_9.setGeometry(QtCore.QRect(10, 320, 101, 20))
        self.label_9.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.dateofbirth_2 = QtWidgets.QLabel(self.Update_details)
        self.dateofbirth_2.setGeometry(QtCore.QRect(10, 270, 121, 19))

        self.dateofbirth_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirth_2.setObjectName("dateofbirth_2")
        self.departmentLine = QtWidgets.QLineEdit(self.Update_details)
        self.departmentLine.setGeometry(QtCore.QRect(143, 324, 181, 31))
        self.departmentLine.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.departmentLine.setObjectName("departmentLine")
        self.UpdateProfile = QtWidgets.QPushButton(self.Update_details)
        self.UpdateProfile.setGeometry(QtCore.QRect(350, 420, 281, 41))
        self.UpdateProfile.setMouseTracking(True)
        self.UpdateProfile.setTabletTracking(True)
        self.UpdateProfile.setAutoFillBackground(False)
        self.UpdateProfile.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-update-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpdateProfile.setIcon(icon1)
        self.UpdateProfile.setIconSize(QtCore.QSize(40, 40))
        self.UpdateProfile.setObjectName("UpdateProfile")
        self.UploadPicture = QtWidgets.QPushButton(self.Update_details)
        self.UploadPicture.setGeometry(QtCore.QRect(670, 280, 171, 41))
        self.UploadPicture.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.UploadPicture.setObjectName("UploadPicture")
        self.ImageLabel = QtWidgets.QLabel(self.Update_details)
        self.ImageLabel.setGeometry(QtCore.QRect(770, -130, 81, 121))
        self.ImageLabel.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.ImageLabel.setText("")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.dateofBirth = QtWidgets.QLineEdit(self.Update_details)
        self.dateofBirth.setGeometry(QtCore.QRect(140, 270, 191, 31))
        self.dateofBirth.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dateofBirth.setObjectName("dateofBirth")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-profile-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Update_details, icon2, "")
        self.MarksheetStudent = QtWidgets.QWidget()
        self.MarksheetStudent.setObjectName("MarksheetStudent")
        self.Marksheet = QtWidgets.QTableWidget(self.MarksheetStudent)
        self.Marksheet.setGeometry(QtCore.QRect(10, 60, 751, 391))
        self.Marksheet.setStyleSheet("Background:white;\n"
"border:1px solid  #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Marksheet.setObjectName("Marksheet")
        self.Marksheet.setColumnCount(7)
        self.Marksheet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.Marksheet.setHorizontalHeaderItem(6, item)
        self.getMarksheet = QtWidgets.QPushButton(self.MarksheetStudent)
        self.getMarksheet.setGeometry(QtCore.QRect(780, 60, 221, 41))
        self.getMarksheet.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-refresh-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getMarksheet.setIcon(icon3)
        self.getMarksheet.setIconSize(QtCore.QSize(30, 30))
        self.getMarksheet.setObjectName("getMarksheet")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-grades-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.MarksheetStudent, icon4, "")
        self.Student_Courses_tab = QtWidgets.QWidget()
        self.Student_Courses_tab.setObjectName("Student_Courses_tab")
        self.full_name_2 = QtWidgets.QLabel(self.Student_Courses_tab)
        self.full_name_2.setGeometry(QtCore.QRect(120, 80, 221, 31))
        self.full_name_2.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name_2.setObjectName("full_name_2")
        self.StudentCourses = QtWidgets.QListWidget(self.Student_Courses_tab)
        self.StudentCourses.setGeometry(QtCore.QRect(120, 140, 591, 221))
        self.StudentCourses.setStyleSheet("Background:white;\n"
"border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.StudentCourses.setObjectName("StudentCourses")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-course-assign-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Student_Courses_tab, icon5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.full_name_4 = QtWidgets.QLabel(self.tab_3)
        self.full_name_4.setGeometry(QtCore.QRect(40, 20, 71, 21))

        self.full_name_4.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name_4.setObjectName("full_name_4")
        self.IATs = QtWidgets.QComboBox(self.tab_3)
        self.IATs.setGeometry(QtCore.QRect(130, 20, 131, 31))
        self.IATs.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.IATs.setObjectName("IATs")
        self.IATs.addItem("")
        self.IATs.setItemText(0, "")
        self.IATs.addItem("")
        self.IATs.addItem("")
        self.getIATGraph = QtWidgets.QPushButton(self.tab_3)
        self.getIATGraph.setGeometry(QtCore.QRect(290, 20, 101, 41))
        self.getIATGraph.setMouseTracking(True)
        self.getIATGraph.setTabletTracking(True)

        self.getIATGraph.setAutoFillBackground(False)
        self.getIATGraph.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-login-rounded-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getIATGraph.setIcon(icon6)
        self.getIATGraph.setIconSize(QtCore.QSize(40, 40))
        self.getIATGraph.setObjectName("getIATGraph")
        self.ATs = QtWidgets.QComboBox(self.tab_3)
        self.ATs.setGeometry(QtCore.QRect(720, 21, 131, 31))
        self.ATs.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.ATs.setObjectName("ATs")
        self.ATs.addItem("")
        self.ATs.setItemText(0, "")
        self.ATs.addItem("")
        self.ATs.addItem("")
        self.full_name_7 = QtWidgets.QLabel(self.tab_3)
        self.full_name_7.setGeometry(QtCore.QRect(630, 20, 71, 21))
  
        self.full_name_7.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name_7.setObjectName("full_name_7")
        self.getATGraph = QtWidgets.QPushButton(self.tab_3)
        self.getATGraph.setGeometry(QtCore.QRect(890, 20, 101, 41))
        self.getATGraph.setMouseTracking(True)
        self.getATGraph.setTabletTracking(True)

        self.getATGraph.setAutoFillBackground(False)
        self.getATGraph.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.getATGraph.setIcon(icon6)
        self.getATGraph.setIconSize(QtCore.QSize(40, 40))
        self.getATGraph.setObjectName("getATGraph")
        self.IAT1_image = QtWidgets.QLabel(self.tab_3)
        self.IAT1_image.setGeometry(QtCore.QRect(10, 70, 501, 391))
        self.IAT1_image.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.IAT1_image.setObjectName("IAT1_image")
        self.IAT1_image.setScaledContents(True)
        self.AT2_image = QtWidgets.QLabel(self.tab_3)
        self.AT2_image.setGeometry(QtCore.QRect(550, 70, 501, 391))
        self.AT2_image.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.AT2_image.setText("")
        self.AT2_image.setObjectName("AT2_image")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-increase-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon7, "")
        self.ImageLabel_2 = QtWidgets.QLabel(StudentScreen)
        self.ImageLabel_2.setGeometry(QtCore.QRect(970, 20, 81, 111))
        self.ImageLabel_2.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.ImageLabel_2.setText("")
        self.ImageLabel_2.setScaledContents(True)
        self.ImageLabel_2.setObjectName("ImageLabel_2")
        self.AT2_image.setScaledContents(True)
        self.GraphAreaWidget = QtWidgets.QWidget(self.tab_3)
        self.GraphAreaWidget.setGeometry(QtCore.QRect(0,0,1,1))
        self.GraphAreaWidget.setObjectName("GraphAreaWidget")
        self.GetData(self.Student_PID)
        self.LoadIntoTableStudent()
        self.GetCoursesList(self.Student_PID)
        self.GenderLine.setReadOnly(True)
        self.fullnameLine.setReadOnly(True)
        self.dateofBirth.setReadOnly(True)
        self.departmentLine.setReadOnly(True)
        self.UpdateProfile.clicked.connect(self.UpdateData)
        self.UploadPicture.clicked.connect(self.openImage)
        self.getIATGraph.clicked.connect(self.LoadGraphforIATs)
        self.getATGraph.clicked.connect(self.LoadGraphforATs)
        self.retranslateUi(StudentScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StudentScreen)

    def retranslateUi(self, StudentScreen):
        _translate = QtCore.QCoreApplication.translate
        StudentScreen.setWindowTitle(_translate("StudentScreen", f"Screen of {self.Student_Name}"))
        self.Studentwelcome.setText(_translate("StudentScreen", f"Welcome ,{self.Student_Name}"))
        self.full_name.setToolTip(_translate("StudentScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.address.setText(_translate("StudentScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Address</span></p></body></html>"))
        self.gender.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Gender</span></p></body></html>"))
        self.password_2.setText(_translate("StudentScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.phone_number_2.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        self.email_id_2.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email-ID</span></p></body></html>"))
        self.label_9.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Department</span></p></body></html>"))
        self.dateofbirth_2.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Date Of Birth</span></p></body></html>"))
        self.UpdateProfile.setText(_translate("StudentScreen", "UPDATE PROFILE"))
        self.UploadPicture.setText(_translate("StudentScreen", "Re-Upload Picture"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Update_details), _translate("StudentScreen", "Your Profile"))
        item = self.Marksheet.horizontalHeaderItem(0)
        item.setText(_translate("StudentScreen", "COURSE ID"))
        item = self.Marksheet.horizontalHeaderItem(1)
        item.setText(_translate("StudentScreen", "IAT-1"))
        item = self.Marksheet.horizontalHeaderItem(2)
        item.setText(_translate("StudentScreen", "IAT-2"))
        item = self.Marksheet.horizontalHeaderItem(3)
        item.setText(_translate("StudentScreen", "IAT AVERAGE"))
        item = self.Marksheet.horizontalHeaderItem(4)
        item.setText(_translate("StudentScreen", "AT-1"))
        item = self.Marksheet.horizontalHeaderItem(5)
        item.setText(_translate("StudentScreen", "AT-2"))
        item = self.Marksheet.horizontalHeaderItem(6)
        item.setText(_translate("StudentScreen", "AT AVERAGE"))
        self.getMarksheet.setText(_translate("StudentScreen", "GET MARKSHEET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MarksheetStudent), _translate("StudentScreen", "Your Marksheet"))
        self.full_name_2.setToolTip(_translate("StudentScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name_2.setText(_translate("StudentScreen", "<html><head/><body><p>Your Courses to Study:</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Student_Courses_tab), _translate("StudentScreen", "Your Current Courses"))
        self.full_name_4.setToolTip(_translate("StudentScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name_4.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Select:</span></p></body></html>"))
        self.IATs.setItemText(1, _translate("StudentScreen", "IAT-1"))
        self.IATs.setItemText(2, _translate("StudentScreen", "IAT-2"))
        self.getIATGraph.setText(_translate("StudentScreen", "GET "))
        self.ATs.setItemText(1, _translate("StudentScreen", "AT-1"))
        self.ATs.setItemText(2, _translate("StudentScreen", "AT-2"))
        self.full_name_7.setToolTip(_translate("StudentScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name_7.setText(_translate("StudentScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Select:</span></p></body></html>"))
        self.getATGraph.setText(_translate("StudentScreen", "GET "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("StudentScreen", "Where You Stand"))


    def ToLogOut(self):
        try:

            os.remove(f"IAT_1_{self.Student_PID}.png") 
            os.remove(f"IAT_2_{self.Student_PID}.png") 
            os.remove(f"AT_1_{self.Student_PID}.png") 
            os.remove(f"AT_2_{self.Student_PID}.png") 
        except Exception as e:
            pass
        app.quit()


    def LoadGraphforATs(self):
        ChoiceOfExam=self.ATs.currentText()
        if ChoiceOfExam!="":
            if ChoiceOfExam=="AT-1":
                try:

                    self.canvas = CanvasAT1(self.GraphAreaWidget, width=8, height=6,pid=self.Student_PID)
                    self.canvas.move(0,0)
                    time.sleep(3)

                    image=f'AT_1_{self.Student_PID}.png'
                    self.AT2_image.setPixmap(QtGui.QPixmap(image))
                except Exception as err:
                    self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")  
            elif ChoiceOfExam=="AT-2":
                try:
                    self.canvas = CanvasAT2(self.GraphAreaWidget, width=8, height=6,pid=self.Student_PID)
                    self.canvas.move(0,0)
                    time.sleep(3)
                    image2=f'AT_2_{self.Student_PID}.png'
                    self.AT2_image.setPixmap(QtGui.QPixmap(image2))
                except Exception as err:
                    self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")  
        else:
            self.warning("Nothing Selected","Please Select An Exam")

    def LoadGraphforIATs(self):

        ChoiceOfExam=self.IATs.currentText()
        if ChoiceOfExam!="":
            if ChoiceOfExam=="IAT-1":
                try:
                    self.canvas = CanvasIAT1(self.GraphAreaWidget, width=8, height=6,pid=self.Student_PID)
                    self.canvas.move(0,0)
                    time.sleep(3)

                    image=f'IAT_1_{self.Student_PID}.png'
                    self.IAT1_image.setPixmap(QtGui.QPixmap(image))
                except Exception as err:
                    self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")    
            elif ChoiceOfExam=="IAT-2":
                try:

                    self.canvas = CanvasIAT2(self.GraphAreaWidget, width=8, height=6,pid=self.Student_PID)
                    self.canvas.move(0,0)
                    time.sleep(3)
                    image2=f'IAT_2_{self.Student_PID}.png'
                    self.IAT1_image.setPixmap(QtGui.QPixmap(image2))
                except Exception as err:
                    self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")  
        else:
            self.warning("Nothing Selected","Please Select An Exam")


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


    def GetCoursesList(self,PID):
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        self.StudentCourses.clear()
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        Query="SELECT crs.course_id,crs.course_name  FROM takes tk, course crs where crs.course_id=tk.course_id and tk.PID=%s;"
        cursor=conn.cursor()
        cursor.execute(Query,PID)
        records=cursor.fetchall()
        print(records)
        crs_List=[]
        for i in range(len(records)):
            temp=f"{records[i][0]}--->{records[i][1]}"
            crs_List.append(temp)

        
        self.StudentCourses.addItems(crs_List)
        conn.commit()
        conn.close()

    def LoadIntoTableStudent(self):
        
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT distinct(crs.course_name), es.IAT_1, es.IAT_2, es.IAT_AVG, es.AT_1, es.AT_2, es.AT_AVG from exam_scheme es,course crs where PID=%s and crs.course_id=es.course_id;"
        cursor.execute(query,(self.Student_PID))
        result=cursor.fetchall()
        self.Marksheet.setRowCount(0)
        header=self.Marksheet.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for row_no,row_data in enumerate(result):
            self.Marksheet.insertRow(row_no)
            for column_no,data in enumerate(row_data):
                self.Marksheet.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))  

        self.Marksheet.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def openImage(self):
        global strimg
        self.url=QFileDialog.getOpenFileName()
        strimg=str(self.url[0])
        self.ImageLabel_2.setPixmap(QtGui.QPixmap(strimg)) 
    
    def convertToBinaryData(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def UpdateData(self):
        global strimg
        global urlofImage
        PID=self.Student_PID
        passwordIn=self.password.text()
        addressIn=self.AddressLine.toPlainText()
        phNumberIn=self.phone_numberline.text()
        emailidIn=self.email_idline.text()
        
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        try:

            host="localhost"
            port=3306;dbname="studentDBMS";user="root";password1="reuben"
            conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
            cursor=conn.cursor()
            QueryToGetData="SELECT profile_picture FROM studentDBMS.student_registration where PID=%s"
            cursor.execute(QueryToGetData,PID)
            pp=cursor.fetchall()
            print(pp[0][0])
            urlofImage=pp[0][0]
            urlofImage=self.convertToBinaryData(strimg)
        except Exception as Err:
            self.messagebox("MARKS NOT INSERTED",f"{err}")

        updateargs=(addressIn,passwordIn,phNumberIn,emailidIn,dt_string,str(urlofImage),PID)
        QueryToGetData="UPDATE student_registration set address=%s,passwd=%s,phone_no=%s,email_id=%s,last_login_time_date=%s,profile_picture=%s where PID=%s"
        cursor.execute(QueryToGetData,updateargs)
        conn.commit()
        conn.close()
        self.messagebox("Successfully Updated Data","Update Your Data Successful")      

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowIcon(QtGui.QIcon('education.ico'))
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()


    def GetData(self,pid):
        _translate = QtCore.QCoreApplication.translate
        
        PID=pid
        host="localhost"
        port=3306;dbname="studentDBMS";user="root";password1="reuben"
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        cursor=conn.cursor()
        QueryToGetData="SELECT * FROM studentDBMS.student_registration where pid=%s"
        cursor.execute(QueryToGetData,PID)
        records=cursor.fetchall()
        print(records)
        self.fullnameLine.setText(_translate("Dialog",f"{records[0][1]}"))
        self.email_idline.setText(_translate("Dialog",f"{records[0][7]}"))
        self.dateofBirth.setText(_translate("Dialog",f"{records[0][4]}"))
        self.GenderLine.setText(_translate("Dialog",f"{records[0][5]}"))
        self.phone_numberline.setText(_translate("Dialog",f"{records[0][3]}"))
        self.password.setText(_translate("Dialog",f"{records[0][6]}"))
        self.departmentLine.setText(_translate("Dialog",f"{records[0][8]}"))
        self.AddressLine.setText(_translate("Dialog",f"{records[0][2]}"))

        try:
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(records[0][11])
            self.ImageLabel_2.setPixmap(QtGui.QPixmap(pixmap))
        except Exception as err:
            pass
        conn.commit()
        conn.close()


class CanvasIAT2(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 60,pid=0000):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.pid=pid
        #self.axes.bar('subjects')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()
        fig.savefig(f'IAT_2_{self.pid}.png')
        


    def plot(self):
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        try:
            conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
            print("connection successful")
            Query="SELECT crs.course_name,es.IAT_2 from exam_scheme es,course crs where PID=%s and crs.course_id=es.course_id"
            cursor=conn.cursor()
            cursor.execute(Query,self.pid)
            records=cursor.fetchall()
            print(records)
            marksGot=[]
            for i in range(len(records)):
                marksGot.append(records[i][1])
            # Generate dummy data into a dataframe

            cursor2=conn.cursor()
            queryToGetCourses="SELECT crs.course_id,crs.course_name  FROM takes tk, course crs where crs.course_id=tk.course_id and tk.PID=%s"
            cursor2.execute(queryToGetCourses,self.pid)
            coursesAssigned=cursor2.fetchall()
            print(coursesAssigned)
            courseList=[]
            for i in range(len(coursesAssigned)):
                courseList.append(str(coursesAssigned[i][0]))
                print(coursesAssigned[i][0])
            print(courseList)
            HighestMarks=[]
            for i in range(len(courseList)):
                cursor3=conn.cursor()
                queryToGetMax=f"SELECT max(IAT_2) from studentDBMS.exam_scheme where course_id=\"{courseList[i]}\";"
                print(queryToGetMax)
                cursor3.execute(queryToGetMax)
                marksHI=cursor3.fetchall()
                HighestMarks.append(marksHI[0][0])
            print(HighestMarks)

            query=""
                   
            index = np.arange(5)
            bar_width = 0.35
            
            ax = self.figure.add_subplot(111)
            summer = ax.bar(index,marksGot, bar_width,label="Marks Obtained")
            
            winter = ax.bar(index+bar_width,HighestMarks , bar_width, label="Highest Marks")
            
            ax.set_xlabel('Category')
            ax.set_ylabel('Marks')
            ax.set_title('Where You Stand in your Class')
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(courseList)        
        except Exception as err:
            self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")    

class CanvasAT2(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 60,pid=0000):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.pid=pid
        #self.axes.bar('subjects')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()
        fig.savefig(f'AT_2_{self.pid}.png')
        


    def plot(self):
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        try:
            conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
            # print("connection successful")
            Query="SELECT crs.course_name,es.AT_2 from exam_scheme es,course crs where PID=%s and crs.course_id=es.course_id"
            cursor=conn.cursor()
            cursor.execute(Query,self.pid)
            records=cursor.fetchall()
            # print(records)
            marksGot=[]
            for i in range(len(records)):
                marksGot.append(records[i][1])
            # Generate dummy data into a dataframe

            cursor2=conn.cursor()
            queryToGetCourses="SELECT crs.course_id,crs.course_name  FROM takes tk, course crs where crs.course_id=tk.course_id and tk.PID=%s"
            cursor2.execute(queryToGetCourses,self.pid)
            coursesAssigned=cursor2.fetchall()
            # print(coursesAssigned)
            courseList=[]
            for i in range(len(coursesAssigned)):
                courseList.append(str(coursesAssigned[i][0]))
                print(coursesAssigned[i][0])
            print(courseList)
            HighestMarks=[]
            for i in range(len(courseList)):
                cursor3=conn.cursor()
                queryToGetMax=f"SELECT max(AT_2) from studentDBMS.exam_scheme where course_id=\"{courseList[i]}\";"
                print(queryToGetMax)
                cursor3.execute(queryToGetMax)
                marksHI=cursor3.fetchall()
                HighestMarks.append(marksHI[0][0])
            # print(HighestMarks)

            query=""
                   
            index = np.arange(5)
            bar_width = 0.35
            
            ax = self.figure.add_subplot(111)
            summer = ax.bar(index,marksGot, bar_width,label="Marks Obtained")
            
            winter = ax.bar(index+bar_width,HighestMarks , bar_width, label="Highest Marks")
            
            ax.set_xlabel('Category')
            ax.set_ylabel('Marks')
            ax.set_title('Where You Stand in your Class')
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(courseList)  
        except Exception as err:
            self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")    

class CanvasAT1(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 60,pid=0000):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.pid=pid
        #self.axes.bar('subjects')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.plot()
        fig.savefig(f'AT_1_{self.pid}.png')
        


    def plot(self):
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        try:
            conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
            # print("connection successful")
            Query="SELECT crs.course_name,es.AT_1 from exam_scheme es,course crs where PID=%s and crs.course_id=es.course_id"
            cursor=conn.cursor()
            cursor.execute(Query,self.pid)
            records=cursor.fetchall()
            # print(records)
            marksGot=[]
            for i in range(len(records)):
                marksGot.append(records[i][1])
            # Generate dummy data into a dataframe

            cursor2=conn.cursor()
            queryToGetCourses="SELECT crs.course_id,crs.course_name  FROM takes tk, course crs where crs.course_id=tk.course_id and tk.PID=%s"
            cursor2.execute(queryToGetCourses,self.pid)
            coursesAssigned=cursor2.fetchall()
            # print(coursesAssigned)
            courseList=[]
            for i in range(len(coursesAssigned)):
                courseList.append(str(coursesAssigned[i][0]))
                print(coursesAssigned[i][0])
            print(courseList)
            HighestMarks=[]
            for i in range(len(courseList)):
                cursor3=conn.cursor()
                queryToGetMax=f"SELECT max(AT_1) from studentDBMS.exam_scheme where course_id=\"{courseList[i]}\";"
                print(queryToGetMax)
                cursor3.execute(queryToGetMax)
                marksHI=cursor3.fetchall()
                HighestMarks.append(marksHI[0][0])
            # print(HighestMarks)

            query=""
                   
            index = np.arange(5)
            bar_width = 0.35
            
            ax = self.figure.add_subplot(111)
            summer = ax.bar(index,marksGot, bar_width,label="Marks Obtained")
            
            winter = ax.bar(index+bar_width,HighestMarks , bar_width, label="Highest Marks")
            
            ax.set_xlabel('Category')
            ax.set_ylabel('Marks')
            ax.set_title('Where You Stand in your Class')
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(courseList)  
        except Exception as err:
            self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")    
class CanvasIAT1(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 5, dpi = 60,pid=0000):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.pid=pid
        #self.axes.bar('subjects')
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        try:

            self.plot()
            fig.savefig(f'IAT_1_{self.pid}.png')
        except Exception as err:
            self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")    
        


    def plot(self):
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        try:

            conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
            # print("connection successful")
            Query="SELECT crs.course_name,es.IAT_1 from exam_scheme es,course crs where PID=%s and crs.course_id=es.course_id"
            cursor=conn.cursor()
            cursor.execute(Query,self.pid)
            records=cursor.fetchall()
            # print(records)
            marksGot=[]
            for i in range(len(records)):
                marksGot.append(records[i][1])
            # Generate dummy data into a dataframe

            cursor2=conn.cursor()
            queryToGetCourses="SELECT crs.course_id,crs.course_name  FROM takes tk, course crs where crs.course_id=tk.course_id and tk.PID=%s"
            cursor2.execute(queryToGetCourses,self.pid)
            coursesAssigned=cursor2.fetchall()
            # print(coursesAssigned)
            courseList=[]
            for i in range(len(coursesAssigned)):
                courseList.append(str(coursesAssigned[i][0]))
                print(coursesAssigned[i][0])
            print(courseList)
            HighestMarks=[]
            for i in range(len(courseList)):
                cursor3=conn.cursor()
                queryToGetMax=f"SELECT max(IAT_1) from studentDBMS.exam_scheme where course_id=\"{courseList[i]}\";"
                print(queryToGetMax)
                cursor3.execute(queryToGetMax)
                marksHI=cursor3.fetchall()
                HighestMarks.append(marksHI[0][0])
            # print(HighestMarks)

            query=""
                   
            index = np.arange(5)
            bar_width = 0.35
            
            ax = self.figure.add_subplot(111)
            summer = ax.bar(index,marksGot, bar_width,label="Marks Obtained")
            
            winter = ax.bar(index+bar_width,HighestMarks , bar_width, label="Highest Marks")
            
            ax.set_xlabel('Category')
            ax.set_ylabel('Marks')
            ax.set_title('Where You Stand in your Class')
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(courseList)
        except Exception as err:
            self.warning("Error Plotting or No Plot",f"{err} Or Graph Doesn't Exist")        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentScreen = QtWidgets.QDialog()
    ui = Ui_StudentScreen(181036,"1234")
    ui.setupUi(StudentScreen)
    StudentScreen.show()
    sys.exit(app.exec_())
