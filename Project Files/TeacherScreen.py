


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
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import images_rc
from requests import get


class Ui_AdminScreen(object):
    def __init__(self,facPID,FacPass):
        self.faculty_PID=facPID
        self.faculty_pass=FacPass
        host="localhost";port=3306;dbname="studentDBMS";user="root";password1="reuben"
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        cursor=conn.cursor()
        query="SELECT full_name,dept_id FROM studentDBMS.faculty WHERE fac_id=%s and Passwd=%s"
        args=(self.faculty_PID,self.faculty_pass)
        cursor.execute(query,args)
        records=cursor.fetchall()
        self.faculty_Name=records[0][0]
        self.faculty_department=records[0][1]
        conn.commit()
        conn.close()
    def setupUi(self, AdminScreen):
        AdminScreen.setObjectName("AdminScreen")
        AdminScreen.resize(1138, 675)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/education.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdminScreen.setWindowIcon(icon)
        AdminScreen.setStyleSheet("background-color:#c5eff7;")
        self.AdminWelcome = QtWidgets.QPushButton(AdminScreen)
        self.AdminWelcome.setGeometry(QtCore.QRect(300, 30, 481, 41))
        self.AdminWelcome.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-teacher-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminWelcome.setIcon(icon1)
        self.AdminWelcome.setIconSize(QtCore.QSize(40, 40))
        self.AdminWelcome.setObjectName("AdminWelcome")
        self.AdminScreenTabs = QtWidgets.QTabWidget(AdminScreen)
        self.AdminScreenTabs.setGeometry(QtCore.QRect(20, 100, 1091, 551))
        self.AdminScreenTabs.setAutoFillBackground(False)
        self.AdminScreenTabs.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 10px;\n"
"border:1px solid #c5eff7;\n"
"")
        self.AdminScreenTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.AdminScreenTabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.AdminScreenTabs.setIconSize(QtCore.QSize(30, 30))
        self.AdminScreenTabs.setObjectName("AdminScreenTabs")
        self.Add_Teacher = QtWidgets.QWidget()
        self.Add_Teacher.setObjectName("Add_Teacher")
        self.email_id_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.email_id_2.setGeometry(QtCore.QRect(470, 320, 81, 19))
        self.email_id_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.email_id_2.setObjectName("email_id_2")
        self.email_id_In = QtWidgets.QLineEdit(self.Add_Teacher)
        self.email_id_In.setGeometry(QtCore.QRect(610, 320, 231, 31))
        self.email_id_In.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.email_id_In.setObjectName("email_id_In")
        self.gender = QtWidgets.QLabel(self.Add_Teacher)
        self.gender.setGeometry(QtCore.QRect(80, 160, 71, 19))
        self.gender.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.gender.setObjectName("gender")
        self.dateofbirth_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.dateofbirth_2.setGeometry(QtCore.QRect(470, 270, 121, 19))

        self.dateofbirth_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirth_2.setObjectName("dateofbirth_2")
        self.address = QtWidgets.QLabel(self.Add_Teacher)
        self.address.setGeometry(QtCore.QRect(480, 90, 71, 19))
        self.address.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.address.setObjectName("address")
        self.full_name = QtWidgets.QLabel(self.Add_Teacher)
        self.full_name.setGeometry(QtCore.QRect(80, 90, 91, 19))
        self.full_name.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name.setObjectName("full_name")
        self.label_10 = QtWidgets.QLabel(self.Add_Teacher)
        self.label_10.setGeometry(QtCore.QRect(80, 420, 111, 31))
        self.label_10.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.Add_Teacher)
        self.label_9.setGeometry(QtCore.QRect(80, 370, 111, 21))
        self.label_9.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.phone_number_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.phone_number_2.setGeometry(QtCore.QRect(470, 370, 131, 19))
        self.phone_number_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.phone_number_2.setObjectName("phone_number_2")
        self.Qulaification = QtWidgets.QLabel(self.Add_Teacher)
        self.Qulaification.setGeometry(QtCore.QRect(80, 310, 121, 31))
        self.Qulaification.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Qulaification.setObjectName("Qulaification")
        self.fullnameIn = QtWidgets.QLineEdit(self.Add_Teacher)
        self.fullnameIn.setGeometry(QtCore.QRect(250, 90, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullnameIn.sizePolicy().hasHeightForWidth())
        self.fullnameIn.setSizePolicy(sizePolicy)
        self.fullnameIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.fullnameIn.setObjectName("fullnameIn")
        self.password_2 = QtWidgets.QLabel(self.Add_Teacher)
        self.password_2.setGeometry(QtCore.QRect(80, 220, 91, 19))
        self.password_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.password_2.setObjectName("password_2")
        self.AddressIn = QtWidgets.QTextEdit(self.Add_Teacher)
        self.AddressIn.setGeometry(QtCore.QRect(610, 90, 221, 81))
        self.AddressIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.AddressIn.setObjectName("AddressIn")
        self.passwordIn = QtWidgets.QLineEdit(self.Add_Teacher)
        self.passwordIn.setGeometry(QtCore.QRect(250, 220, 191, 31))
        self.passwordIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.passwordIn.setObjectName("passwordIn")
        self.phone_numberIn = QtWidgets.QLineEdit(self.Add_Teacher)
        self.phone_numberIn.setGeometry(QtCore.QRect(610, 370, 231, 31))
        self.phone_numberIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.phone_numberIn.setObjectName("phone_numberIn")
        self.Qualif_In = QtWidgets.QComboBox(self.Add_Teacher)
        self.Qualif_In.setGeometry(QtCore.QRect(250, 319, 191, 31))
        self.Qualif_In.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Qualif_In.setObjectName("Qualif_In")
        self.depart_In = QtWidgets.QLineEdit(self.Add_Teacher)
        self.depart_In.setGeometry(QtCore.QRect(250, 369, 191, 31))
        self.depart_In.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.depart_In.setObjectName("depart_In")
        self.Experi_In = QtWidgets.QComboBox(self.Add_Teacher)
        self.Experi_In.setGeometry(QtCore.QRect(250, 420, 191, 31))
        self.Experi_In.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Experi_In.setObjectName("Experi_In")
        self.dateOfbirthIn = QtWidgets.QLineEdit(self.Add_Teacher)
        self.dateOfbirthIn.setGeometry(QtCore.QRect(610, 260, 231, 31))
        self.dateOfbirthIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dateOfbirthIn.setObjectName("dateOfbirthIn")
        self.GenderIn = QtWidgets.QLineEdit(self.Add_Teacher)
        self.GenderIn.setGeometry(QtCore.QRect(250, 150, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GenderIn.sizePolicy().hasHeightForWidth())
        self.GenderIn.setSizePolicy(sizePolicy)
        self.GenderIn.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.GenderIn.setObjectName("GenderIn")


        self.UpdateProfile = QtWidgets.QPushButton(self.Add_Teacher)
        self.UpdateProfile.setGeometry(QtCore.QRect(410, 460, 240, 41))
        self.UpdateProfile.setMouseTracking(True)
        self.UpdateProfile.setTabletTracking(True)
        self.UpdateProfile.setAutoFillBackground(False)
        self.UpdateProfile.setStyleSheet("background-color:#1e8bc3;\n"
        "border-radius: 15px;\n"
        "color:white;\n"
        "font: 25 16pt \"Microsoft YaHei UI Light\";\n"
        "border:3px solid white;\n"
        "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-update-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UpdateProfile.setIcon(icon)
        self.UpdateProfile.setIconSize(QtCore.QSize(40, 40))
        self.UpdateProfile.setObjectName("UpdateProfile")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-add-administrator-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.Add_Teacher, icon2, "")
        self.teacher_Details = QtWidgets.QWidget()
        self.teacher_Details.setObjectName("teacher_Details")
        self.Submit_AT2 = QtWidgets.QPushButton(self.teacher_Details)
        self.Submit_AT2.setGeometry(QtCore.QRect(670, 470, 91, 41))
        self.Submit_AT2.setMouseTracking(True)
        self.Submit_AT2.setTabletTracking(True)
        self.Submit_AT2.setAutoFillBackground(False)
        self.Submit_AT2.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 15pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-submit-for-approval-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Submit_AT2.setIcon(icon3)
        self.Submit_AT2.setIconSize(QtCore.QSize(30, 30))
        self.Submit_AT2.setObjectName("Submit_AT2")
        self.Marksheet = QtWidgets.QTableWidget(self.teacher_Details)
        self.Marksheet.setGeometry(QtCore.QRect(20, 70, 841, 391))
        self.Marksheet.setStyleSheet("Background:white;\n"
"border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Marksheet.setObjectName("Marksheet")
        self.Marksheet.setColumnCount(8)
        self.Marksheet.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Marksheet.setHorizontalHeaderItem(7, item)
        self.Submit_IAT2 = QtWidgets.QPushButton(self.teacher_Details)
        self.Submit_IAT2.setGeometry(QtCore.QRect(320, 470, 91, 41))
        self.Submit_IAT2.setMouseTracking(True)
        self.Submit_IAT2.setTabletTracking(True)

        self.Submit_IAT2.setAutoFillBackground(False)
        self.Submit_IAT2.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 15pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Submit_IAT2.setIcon(icon3)
        self.Submit_IAT2.setIconSize(QtCore.QSize(30, 30))
        self.Submit_IAT2.setObjectName("Submit_IAT2")
        self.Courses = QtWidgets.QComboBox(self.teacher_Details)
        self.Courses.setGeometry(QtCore.QRect(220, 20, 231, 31))
        self.Courses.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Courses.setObjectName("Courses")

        self.Submit_IAT1 = QtWidgets.QPushButton(self.teacher_Details)
        self.Submit_IAT1.setGeometry(QtCore.QRect(200, 470, 91, 41))
        self.Submit_IAT1.setMouseTracking(True)
        self.Submit_IAT1.setTabletTracking(True)

        self.Submit_IAT1.setAutoFillBackground(False)
        self.Submit_IAT1.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 15pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Submit_IAT1.setIcon(icon3)
        self.Submit_IAT1.setIconSize(QtCore.QSize(30, 30))
        self.Submit_IAT1.setObjectName("Submit_IAT1")

        self.UploadPicture = QtWidgets.QPushButton(self.Add_Teacher)
        self.UploadPicture.setGeometry(QtCore.QRect(850, 10, 171, 41))
        self.UploadPicture.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.UploadPicture.setObjectName("UploadPicture")
        self.Course_ID_Label = QtWidgets.QLabel(self.teacher_Details)
        self.Course_ID_Label.setGeometry(QtCore.QRect(70, 10, 111, 41))
        self.Course_ID_Label.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Course_ID_Label.setObjectName("Course_ID_Label")
        self.getMarksheet = QtWidgets.QPushButton(self.teacher_Details)
        self.getMarksheet.setGeometry(QtCore.QRect(510, 10, 221, 41))
        self.getMarksheet.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-refresh-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getMarksheet.setIcon(icon4)
        self.getMarksheet.setIconSize(QtCore.QSize(30, 30))
        self.getMarksheet.setObjectName("getMarksheet")
        self.Submit_AT1 = QtWidgets.QPushButton(self.teacher_Details)
        self.Submit_AT1.setGeometry(QtCore.QRect(540, 470, 91, 41))
        self.Submit_AT1.setMouseTracking(True)
        self.Submit_AT1.setTabletTracking(True)
        self.Submit_AT1.setAutoFillBackground(False)
        self.Submit_AT1.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 15pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Submit_AT1.setIcon(icon3)
        self.Submit_AT1.setIconSize(QtCore.QSize(30, 30))
        self.Submit_AT1.setObjectName("Submit_AT1")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-teacher-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.teacher_Details, icon5, "")
        self.Student_details = QtWidgets.QWidget()
        self.Student_details.setObjectName("Student_details")
        self.studentDetails = QtWidgets.QTableWidget(self.Student_details)
        self.studentDetails.setGeometry(QtCore.QRect(10, 60, 671, 451))
        self.studentDetails.setStyleSheet("Background:white;\n"
"border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.studentDetails.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.studentDetails.setRowCount(5)
        self.studentDetails.setObjectName("studentDetails")
        self.studentDetails.setColumnCount(6)
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
        self.studentDetails.horizontalHeader().setMinimumSectionSize(33)
        self.Refresh_Student = QtWidgets.QPushButton(self.Student_details)
        self.Refresh_Student.setGeometry(QtCore.QRect(710, 60, 51, 41))
        self.Refresh_Student.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.Refresh_Student.setText("")
        self.Refresh_Student.setIcon(icon4)
        self.Refresh_Student.setIconSize(QtCore.QSize(30, 30))
        self.Refresh_Student.setObjectName("Refresh_Student")
        self.label_6 = QtWidgets.QLabel(self.Student_details)
        self.label_6.setGeometry(QtCore.QRect(720, 420, 341, 81))
        self.label_6.setObjectName("label_6")
        self.course_In_StudentDetails = QtWidgets.QComboBox(self.Student_details)
        self.course_In_StudentDetails.setGeometry(QtCore.QRect(190, 20, 231, 31))
        self.course_In_StudentDetails.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.course_In_StudentDetails.setObjectName("course_In_StudentDetails")

        self.Course_ID_Label_2 = QtWidgets.QLabel(self.Student_details)
        self.Course_ID_Label_2.setGeometry(QtCore.QRect(40, 10, 111, 41))
        self.Course_ID_Label_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Course_ID_Label_2.setObjectName("Course_ID_Label_2")
        self.pushButton = QtWidgets.QPushButton(self.Student_details)
        self.pushButton.setGeometry(QtCore.QRect(470, 10, 91, 41))
        self.pushButton.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.pushButton.setObjectName("pushButton")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-student-male-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.Student_details, icon6, "")
        self.CourseAssigned = QtWidgets.QWidget()
        self.CourseAssigned.setObjectName("CourseAssigned")
        self.TeacherCourses = QtWidgets.QListWidget(self.CourseAssigned)
        self.TeacherCourses.setGeometry(QtCore.QRect(140, 140, 591, 221))
        self.TeacherCourses.setStyleSheet("Background:white;\n"
"border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.TeacherCourses.setObjectName("TeacherCourses")
        self.full_name_2 = QtWidgets.QLabel(self.CourseAssigned)
        self.full_name_2.setGeometry(QtCore.QRect(140, 80, 171, 31))
        self.full_name_2.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name_2.setObjectName("full_name_2")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-profile-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AdminScreenTabs.addTab(self.CourseAssigned, icon7, "")
        self.ImageLabel = QtWidgets.QLabel(AdminScreen)
        self.ImageLabel.setGeometry(QtCore.QRect(910, 10, 81, 111))
        self.ImageLabel.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.ImageLabel.setText("")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")

        self.getMarksheet.clicked.connect(self.LoadIntoTableStudent)
        self.GetData(self.faculty_PID)
        self.GetCoursesList(self.faculty_PID)
        self.Submit_AT1.clicked.connect(self.AT1_Submit)
        self.Submit_AT2.clicked.connect(self.AT2_Submit)
        self.Submit_IAT1.clicked.connect(self.IAT1_Submit)
        self.Submit_IAT2.clicked.connect(self.IAT2_Submit)
        self.pushButton.clicked.connect(self.LoadIntoStudentDetails)
        self.studentDetails.cellClicked.connect(self.cell_was_clicked_Student_Table)
        self.UpdateProfile.clicked.connect(self.UpdateData)
        self.UploadPicture.clicked.connect(self.openImage)
        self.retranslateUi(AdminScreen)
        self.AdminScreenTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminScreen)

    def retranslateUi(self, AdminScreen):
        _translate = QtCore.QCoreApplication.translate
        AdminScreen.setWindowTitle(_translate("AdminScreen", f"Faculty Screen of {self.faculty_Name}"))
        self.AdminWelcome.setText(_translate("AdminScreen", f"WELCOME,{self.faculty_Name}"))
        self.UploadPicture.setText(_translate("Dialog", "Re-Upload Picture"))
        self.email_id_2.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Email-ID</span></p></body></html>"))
        self.gender.setText(_translate("AdminScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Gender</span></p></body></html>"))
        self.dateofbirth_2.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Date Of Birth</span></p></body></html>"))
        self.address.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Address</span></p></body></html>"))
        self.full_name.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name.setText(_translate("AdminScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.label_10.setText(_translate("AdminScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Experience</span></p></body></html>"))
        self.label_9.setText(_translate("AdminScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Department</span></p></body></html>"))
        self.phone_number_2.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        self.Qulaification.setText(_translate("AdminScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Qualification</span></p></body></html>"))
        self.password_2.setText(_translate("AdminScreen", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.Add_Teacher), _translate("AdminScreen", "Your Details"))
        self.UpdateProfile.setText(_translate("Dialog", "UPDATE PROFILE"))
        self.Submit_AT2.setText(_translate("AdminScreen", "AT2"))
        item = self.Marksheet.horizontalHeaderItem(0)
        item.setText(_translate("AdminScreen", "PID"))
        item = self.Marksheet.horizontalHeaderItem(1)
        item.setText(_translate("AdminScreen", "STUDENT NAME"))
        item = self.Marksheet.horizontalHeaderItem(2)
        item.setText(_translate("AdminScreen", "IAT-1"))
        item = self.Marksheet.horizontalHeaderItem(3)
        item.setText(_translate("AdminScreen", "IAT-2"))
        item = self.Marksheet.horizontalHeaderItem(4)
        item.setText(_translate("AdminScreen", "IAT AVERAGE"))
        item = self.Marksheet.horizontalHeaderItem(5)
        item.setText(_translate("AdminScreen", "AT-1"))
        item = self.Marksheet.horizontalHeaderItem(6)
        item.setText(_translate("AdminScreen", "AT-2"))
        item = self.Marksheet.horizontalHeaderItem(7)
        item.setText(_translate("AdminScreen", "AT AVERAGE"))
        self.Submit_IAT2.setText(_translate("AdminScreen", "IAT2"))

        self.Submit_IAT1.setText(_translate("AdminScreen", "IAT1"))
        self.Course_ID_Label.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.Course_ID_Label.setText(_translate("AdminScreen", "<html><head/><body><p>Course ID:</p></body></html>"))
        self.getMarksheet.setText(_translate("AdminScreen", "GET MARK SHEET"))
        self.Submit_AT1.setText(_translate("AdminScreen", "AT1"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.teacher_Details), _translate("AdminScreen", "Enter Marks"))
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
        self.label_6.setText(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">CLICK ON A STUDENT PID </span></p><p align=\"center\"><span style=\" font-size:9pt;\">TO SEE COMPLETE DETAILS,</span></p><p align=\"center\"><span style=\" font-size:9pt;\">YOU CAN UPDATE,OR DELETE</span></p><p align=\"center\"><span style=\" font-size:9pt;\">AN FACULTY ALSO</span></p><p align=\"center\"><span style=\" font-size:9pt;\"><br/></span></p></body></html>"))
        # self.course_In_StudentDetails.setItemText(0, _translate("AdminScreen", "_--COURSE--"))

        
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT course_id FROM studentdbms.teaches where fac_id=%s;"
        cursor.execute(query,(self.faculty_PID))
        result=cursor.fetchall()

        for i in range(len(result)):
            self.Courses.addItem("")
            self.Courses.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))
            self.course_In_StudentDetails.addItem("")
            self.course_In_StudentDetails.setItemText(i, _translate("AdminScreen", f"{result[i][0]}"))


        self.Course_ID_Label_2.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.Course_ID_Label_2.setText(_translate("AdminScreen", "<html><head/><body><p>Course ID:</p></body></html>"))
        self.pushButton.setText(_translate("AdminScreen", "GET LIST"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.Student_details), _translate("AdminScreen", "Student Details"))
        self.full_name_2.setToolTip(_translate("AdminScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name_2.setText(_translate("AdminScreen", "<html><head/><body><p>Your Courses are:</p></body></html>"))
        self.AdminScreenTabs.setTabText(self.AdminScreenTabs.indexOf(self.CourseAssigned), _translate("AdminScreen", "Your Courses"))


    def openImage(self):
        global strimg
        self.url=QFileDialog.getOpenFileName()
        strimg=str(self.url[0])
        self.ImageLabel.setPixmap(QtGui.QPixmap(strimg))


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

    def AT2_Submit(self):
        nrows = self.Marksheet.rowCount()
        print(nrows)
        listOfStudents=[]
        AT_1,AT_2,AT_AVG=[],[],[]
        for cell in range(nrows):
            at2v=self.Marksheet.item(cell,6)
            at1v=self.Marksheet.item(cell,5)

            itemPID=self.Marksheet.item(cell,0)
            listOfStudents.append(itemPID.text())

            AT_1.append(at1v.text())
            AT_2.append(at2v.text())
        courseID=self.Courses.currentText()
        
        AT_1=[sub.replace('None',"0") for sub in AT_1]
        AT_2=[sub.replace('None',"0") for sub in AT_2]


        print(AT_1,AT_2)
        print(listOfStudents)
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        at_avg=[]
        temp=[]
        atI,atII=[],[]
        try:
            for cell in range(nrows):
                
                atI.append(float(AT_1[cell]))
                atII.append(float(AT_2[cell]))
                at_avg.append((atI[cell]+atII[cell])/2)
            print(at_avg)            
            for cell in range(nrows):
                conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)

                query="UPDATE exam_scheme Set AT_2=%s,AT_AVG=%s where PID=%s and course_id=%s;"
                cursor=conn.cursor()
                args=(float(AT_2[cell]),float(at_avg[cell]),int(listOfStudents[cell]),courseID)
                
                cursor.execute(query,args)

                conn.commit()
                conn.close()
            self.messagebox("Marks Entered","Marks Entered successfully")
            self.LoadIntoTableStudent()
        except Exception as Err:
            self.messagebox("MARKS NOT INSERTED",f"{err}")
 
    def AT1_Submit(self):
        nrows = self.Marksheet.rowCount()
        print(nrows)
        listOfStudents=[]
        AT_1=[]
        for cell in range(nrows):
            
            at1v=self.Marksheet.item(cell,5)

            itemPID=self.Marksheet.item(cell,0)
            listOfStudents.append(itemPID.text())

            AT_1.append(at1v.text())

        courseID=self.Courses.currentText()
        print(courseID)
        print(AT_1)
        AT_1=[sub.replace('None',"0") for sub in AT_1]
        print(AT_1)
        print(listOfStudents)
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        # Iat_avg=[]
        temp=[]
        # ,float(IAT_2[cell]),float(Iat_avg[cell]),
        try:
 
            for cell in range(nrows):
                conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)

                query="UPDATE exam_scheme Set AT_1=%s where PID=%s and course_id=%s;"
                cursor=conn.cursor()
                args=(float(AT_1[cell]),int(listOfStudents[cell]),courseID)
                
                cursor.execute(query,args)

                conn.commit()
                conn.close()
            self.messagebox("Marks Entered","Marks Entered successfully")
        except Exception as Err:
            self.messagebox("MARKS NOT INSERTED",f"{err}")

    def IAT2_Submit(self):
        nrows = self.Marksheet.rowCount()
        print(nrows)
        IAT_1 = []
        IAT_2=[]
        listOfStudents=[]
        AT_1,AT_2,AT_AVG=[],[],[]
        for cell in range(nrows):

            iat2v=self.Marksheet.item(cell,3)
            iat1v = self.Marksheet.item(cell,2)
            itemPID=self.Marksheet.item(cell,0)
            listOfStudents.append(itemPID.text())
            IAT_1.append(iat1v.text())
            IAT_2.append(iat2v.text())

        courseID=self.Courses.currentText()

        IAT_1=[sub.replace('None',"0") for sub in IAT_1]
        IAT_2=[sub.replace('None',"0") for sub in IAT_2]

        # print(IAT_1,IAT_2)
        # print(listOfStudents)
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        iatI,iatII=[],[]
        Iat_avg=[]
        temp1,temp2=[],[]
        # ,float(IAT_2[cell]),float(Iat_avg[cell]),
        try:
            for cell in range(nrows):
        
                iatI.append(float(IAT_1[cell]))
                iatII.append(float(IAT_2[cell]))


            print(iatI,iatII)
            for cell in range(nrows):
                Iat_avg.append((iatI[cell]+iatII[cell])/2)
            print(Iat_avg)            
            for cell in range(nrows):
                conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)

                query="UPDATE exam_scheme Set IAT_2=%s,IAT_AVG=%s where PID=%s and course_id=%s;"
                cursor=conn.cursor()
                args=(float(IAT_2[cell]),float(Iat_avg[cell]),int(listOfStudents[cell]),courseID)
                
                cursor.execute(query,args)

                conn.commit()
                conn.close()
            self.messagebox("Marks Entered","Marks Entered successfully")
            self.LoadIntoTableStudent()
        except Exception as Err:
            self.messagebox("MARKS NOT INSERTED",f"{Err}")


    def IAT1_Submit(self):
        nrows = self.Marksheet.rowCount()
        print(nrows)
        IAT_1 = []

        listOfStudents=[]
 
        for cell in range(nrows):

            iat1v = self.Marksheet.item(cell,2)
            itemPID=self.Marksheet.item(cell,0)
            listOfStudents.append(itemPID.text())
            IAT_1.append(iat1v.text())

        courseID=self.Courses.currentText()

        IAT_1=[sub.replace('None',"0") for sub in IAT_1]

        # print(IAT_1)
        # print(listOfStudents)
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
    
          
        try:
            for cell in range(nrows):
                conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)

                query="UPDATE exam_scheme Set IAT_1=%s where PID=%s and course_id=%s;"
                cursor=conn.cursor()
                args=(float(IAT_1[cell]),int(listOfStudents[cell]),courseID)
                
                cursor.execute(query,args)

                conn.commit()
                conn.close()
            self.messagebox("Marks Entered","Marks Entered successfully")
        except Exception as Err:
            self.messagebox("MARKS NOT INSERTED",f"{err}")

    def GetCoursesList(self,PID):
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        self.TeacherCourses.clear()
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        Query="SELECT crs.course_id,crs.course_name  FROM teaches th, course crs where crs.course_id=th.course_id and th.fac_id=%s;"
        cursor=conn.cursor()
        cursor.execute(Query,PID)
        records=cursor.fetchall()
        print(records)
        crs_List=[]
        for i in range(len(records)):
            temp=f"{records[i][0]}--->{records[i][1]}"
            crs_List.append(temp)

        
        self.TeacherCourses.addItems(crs_List)
        conn.commit()
        conn.close()

    def GetData(self,pid):
        _translate = QtCore.QCoreApplication.translate
        
        PID=pid
        host="localhost"
        port=3306;dbname="studentDBMS";user="root";password1="reuben"
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        cursor=conn.cursor()
        QueryToGetData="SELECT * FROM studentDBMS.faculty where fac_id=%s"
        cursor.execute(QueryToGetData,PID)
        records=cursor.fetchall()
        print(records)

        self.fullnameIn.setText(_translate("Dialog",f"{records[0][5]}"))
        self.email_id_In.setText(_translate("Dialog",f"{records[0][9]}"))
        self.dateOfbirthIn.setText(_translate("Dialog",f"{records[0][4]}"))
        self.GenderIn.setText(_translate("Dialog",f"{records[0][8]}"))
        self.phone_numberIn.setText(_translate("Dialog",f"{records[0][7]}"))
        self.passwordIn.setText(_translate("Dialog",f"{records[0][1]}"))
        self.depart_In.setText(_translate("Dialog",f"{records[0][2]}"))
        self.AddressIn.setText(_translate("Dialog",f"{records[0][6]}"))

        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        # print("connection successful")
        cursor=conn.cursor()
        query = "SELECT dept_id FROM studentdbms.department;"
        cursor.execute(query)
        result=cursor.fetchall()

        # self.Qualif_In.setText(_translate("Dialog",f"{records[0][3]}"))
        for i in range(4):
            self.Qualif_In.addItem("")
        self.Qualif_In.setItemText(0,_translate("Dialog",f"{records[0][3]}"))
        self.Qualif_In.setItemText(1, _translate("AdminScreen", "Bachelor of Engineering "))
        self.Qualif_In.setItemText(2, _translate("AdminScreen", "Master of Engineering "))
        self.Qualif_In.setItemText(3, _translate("AdminScreen", "PhD in Engineering"))

        # self.Experi_In.setText(_translate("Dialog",f"{records[0][10]}"))
        for i in range(8):
            self.Experi_In.addItem("")
        self.Experi_In.setItemText(0,_translate("Dialog",f"{records[0][10]}"))
        self.Experi_In.setItemText(1, _translate("AdminScreen", "1 Year"))
        self.Experi_In.setItemText(2, _translate("AdminScreen", "2 Years"))
        self.Experi_In.setItemText(3, _translate("AdminScreen", "3 Years"))
        self.Experi_In.setItemText(4, _translate("AdminScreen", "4 Years"))
        self.Experi_In.setItemText(5, _translate("AdminScreen", "5 Years"))
        self.Experi_In.setItemText(6, _translate("AdminScreen", "More Than 5 Years"))
        self.Experi_In.setItemText(7, _translate("AdminScreen", "More Than 10 Years"))

        # print(type(records[0][13]))
        try:

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(records[0][13])
            self.ImageLabel.setPixmap(QtGui.QPixmap(pixmap))
        except Exception as Err:
            pass
        conn.commit()
        conn.close()
    def convertToBinaryData(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    def UpdateData(self):
        global strimg
        global urlofImage
        PID=self.faculty_PID
        passwordIn=self.passwordIn.text()
        addressIn=self.AddressIn.toPlainText()
        phNumberIn=self.phone_numberIn.text()
        emailidIn=self.email_id_In.text()
        experIn=self.Experi_In.currentText()
        QualIn=self.Qualif_In.currentText()
        
        now = datetime.now()
        dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
        try:

            host="localhost"
            port=3306;dbname="studentDBMS";user="root";password1="reuben"
            conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
            cursor=conn.cursor()
            QueryToGetData="SELECT profile_picture FROM studentDBMS.faculty where fac_id=%s"
            cursor.execute(QueryToGetData,PID)
            pp=cursor.fetchall()
            print(pp[0][0])
            urlofImage=pp[0][0]
            urlofImage = self.convertToBinaryData(strimg)
        except Exception as err:
            self.warning("ERROR",f"{err} OR FACULTY DOESNT Exist")
        updateargs=(addressIn,passwordIn,phNumberIn,emailidIn,experIn,QualIn,dt_string,urlofImage,PID)
        
        QueryToGetData="UPDATE studentDBMS.faculty set address=%s,passwd=%s,phone_no=%s,email_id=%s,experience=%s,qualification=%s,login_date_time=%s,profile_picture=%s where fac_id=%s"
        cursor.execute(QueryToGetData,updateargs)
        conn.commit()
        conn.close()
        self.messagebox("Successfully Updated Data","Update Your Data Successful")      
    def openImage(self):
        global strimg
        self.url=QFileDialog.getOpenFileName()
        strimg=str(self.url[0])
        self.ImageLabel.setPixmap(QtGui.QPixmap(strimg)) 

    def LoadIntoTableStudent(self):
        courseID=self.Courses.currentText()
        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT  sr.PID, sr.full_name, es.IAT_1, es.IAT_2, es.IAT_AVG, es.AT_1, es.AT_2, es.AT_AVG FROM student_registration sr, exam_scheme es WHERE sr.PID = es.PID AND es.course_id =%s;"
        cursor.execute(query,courseID)
        result=cursor.fetchall()
        self.Marksheet.setRowCount(0)
        # header=self.tableWidget.horizontalHeader()
        # header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for row_no,row_data in enumerate(result):
            self.Marksheet.insertRow(row_no)
            for column_no,data in enumerate(row_data):
                self.Marksheet.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))
    def LoadIntoStudentDetails(self):
        courseID=self.Courses.currentText()

        host="localhost"
        port=3306
        dbname="studentDBMS"
        user="root"
        password1="reuben"
        pass
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT  distinct(sr.PID), sr.full_name, sr.phone_no, sr.gender, sr.email_id, sr.id_dept FROM student_registration sr,takes tk,course crs WHERE sr.id_dept=crs.dept_id and tk.course_id=%s and sr.id_dept=%s;"
        cursor.execute(query,(courseID,self.faculty_department))
        result=cursor.fetchall()
        self.studentDetails.setRowCount(0)
        header=self.studentDetails.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        for row_no,row_data in enumerate(result):
            self.studentDetails.insertRow(row_no)
            for column_no,data in enumerate(row_data):
                self.studentDetails.setItem(row_no,column_no,QtWidgets.QTableWidgetItem(str(data)))    

    def ToLogOut(self):
    
        AdminScreen.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminScreen = QtWidgets.QDialog()
    ui = Ui_AdminScreen(210030,"1234")
    ui.setupUi(AdminScreen)
    AdminScreen.show()
    sys.exit(app.exec_())
