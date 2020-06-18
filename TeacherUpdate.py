
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


from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time
import images_rc

class Ui_DialogTeacher(object):
    def __init__(self,pid):
        self.pid=pid
        print("PID",self.pid)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(952, 597)
        Dialog.setStyleSheet("background-color:#c5eff7;")
        self.GenderLine = QtWidgets.QLineEdit(Dialog)
        self.GenderLine.setGeometry(QtCore.QRect(203, 214, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GenderLine.sizePolicy().hasHeightForWidth())
        self.GenderLine.setSizePolicy(sizePolicy)
        self.GenderLine.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.GenderLine.setObjectName("GenderLine")
        self.address = QtWidgets.QLabel(Dialog)
        self.address.setGeometry(QtCore.QRect(420, 160, 71, 20))
        self.address.setToolTip("")
        self.address.setWhatsThis("")
        self.address.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.address.setObjectName("address")
        self.fullnameLine = QtWidgets.QLineEdit(Dialog)
        self.fullnameLine.setGeometry(QtCore.QRect(203, 154, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullnameLine.sizePolicy().hasHeightForWidth())
        self.fullnameLine.setSizePolicy(sizePolicy)
        self.fullnameLine.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.fullnameLine.setText("")
        self.fullnameLine.setObjectName("fullnameLine")
        self.gender = QtWidgets.QLabel(Dialog)
        self.gender.setGeometry(QtCore.QRect(50, 220, 71, 19))
        self.gender.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.gender.setObjectName("gender")
        self.UpdateProfile = QtWidgets.QPushButton(Dialog)
        self.UpdateProfile.setGeometry(QtCore.QRect(180, 540, 231, 41))
        self.UpdateProfile.setMouseTracking(True)
        self.UpdateProfile.setTabletTracking(True)
        self.UpdateProfile.setToolTip("")
        self.UpdateProfile.setWhatsThis("")
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
        self.ImageLabel = QtWidgets.QLabel(Dialog)
        self.ImageLabel.setGeometry(QtCore.QRect(790, 150, 81, 121))
        self.ImageLabel.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.ImageLabel.setText("")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.UploadPicture = QtWidgets.QPushButton(Dialog)
        self.UploadPicture.setGeometry(QtCore.QRect(750, 390, 171, 41))
        self.UploadPicture.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.UploadPicture.setObjectName("UploadPicture")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(53, 444, 131, 20))
        self.label_9.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.email_id_2 = QtWidgets.QLabel(Dialog)
        self.email_id_2.setGeometry(QtCore.QRect(50, 330, 91, 20))
        self.email_id_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.email_id_2.setObjectName("email_id_2")
        self.phone_number_2 = QtWidgets.QLabel(Dialog)
        self.phone_number_2.setGeometry(QtCore.QRect(40, 270, 131, 19))
        self.phone_number_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.phone_number_2.setObjectName("phone_number_2")
        self.dateofbirth_2 = QtWidgets.QLabel(Dialog)
        self.dateofbirth_2.setGeometry(QtCore.QRect(50, 390, 121, 19))
        self.dateofbirth_2.setToolTip("")
        self.dateofbirth_2.setWhatsThis("")
        self.dateofbirth_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirth_2.setObjectName("dateofbirth_2")
        self.full_name = QtWidgets.QLabel(Dialog)
        self.full_name.setGeometry(QtCore.QRect(40, 160, 91, 19))
        self.full_name.setWhatsThis("")
        self.full_name.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name.setObjectName("full_name")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(513, 264, 201, 31))
        self.password.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.password.setObjectName("password")
        self.departmentLine = QtWidgets.QLineEdit(Dialog)
        self.departmentLine.setGeometry(QtCore.QRect(203, 444, 191, 31))
        self.departmentLine.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.departmentLine.setObjectName("departmentLine")
        self.phone_numberline = QtWidgets.QLineEdit(Dialog)
        self.phone_numberline.setGeometry(QtCore.QRect(203, 274, 191, 31))
        self.phone_numberline.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.phone_numberline.setObjectName("phone_numberline")
        self.password_2 = QtWidgets.QLabel(Dialog)
        self.password_2.setGeometry(QtCore.QRect(410, 270, 91, 20))
        self.password_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.password_2.setObjectName("password_2")
        self.AddressLine = QtWidgets.QTextEdit(Dialog)
        self.AddressLine.setGeometry(QtCore.QRect(513, 154, 201, 91))
        self.AddressLine.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 12pt \"Microsoft YaHei UI Light\";\n"
"")
        self.AddressLine.setObjectName("AddressLine")
        self.EditWeclomeLabel = QtWidgets.QPushButton(Dialog)
        self.EditWeclomeLabel.setGeometry(QtCore.QRect(210, 40, 491, 51))
        self.EditWeclomeLabel.setStyleSheet("border: 1px solid #1e8bc3;\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/multiple-users-silhouette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditWeclomeLabel.setIcon(icon1)
        self.EditWeclomeLabel.setIconSize(QtCore.QSize(50, 50))
        self.EditWeclomeLabel.setObjectName("EditWeclomeLabel")
        self.email_idline = QtWidgets.QLineEdit(Dialog)
        self.email_idline.setGeometry(QtCore.QRect(203, 334, 511, 31))
        self.email_idline.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.email_idline.setText("")
        self.email_idline.setObjectName("email_idline")
        self.dateodbirthLine = QtWidgets.QLineEdit(Dialog)
        self.dateodbirthLine.setGeometry(QtCore.QRect(203, 384, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateodbirthLine.sizePolicy().hasHeightForWidth())
        self.dateodbirthLine.setSizePolicy(sizePolicy)
        self.dateodbirthLine.setStyleSheet("background-color:white;\n"
"border-radius:15px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.dateodbirthLine.setObjectName("dateodbirthLine")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(423, 444, 111, 31))
        self.label_10.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.Qulaification = QtWidgets.QLabel(Dialog)
        self.Qulaification.setGeometry(QtCore.QRect(413, 385, 121, 31))
        self.Qulaification.setStyleSheet("color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.Qulaification.setObjectName("Qulaification")
        self.Experi_InLine = QtWidgets.QComboBox(Dialog)
        self.Experi_InLine.setGeometry(QtCore.QRect(533, 444, 191, 31))
        self.Experi_InLine.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Experi_InLine.setObjectName("Experi_InLine")
        self.Qualif_In_Line = QtWidgets.QComboBox(Dialog)
        self.Qualif_In_Line.setGeometry(QtCore.QRect(533, 384, 191, 31))
        self.Qualif_In_Line.setStyleSheet("background-color:white;\n"
"border-radius:10px;\n"
"color:#1e8bc3;\n"
"border: 1px solid #1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"")
        self.Qualif_In_Line.setObjectName("Qualif_In_Line")
        self.Delete_Profile = QtWidgets.QPushButton(Dialog)
        self.Delete_Profile.setGeometry(QtCore.QRect(460, 540, 231, 41))
        self.Delete_Profile.setMouseTracking(True)
        self.Delete_Profile.setTabletTracking(True)
        self.Delete_Profile.setToolTip("")
        self.Delete_Profile.setWhatsThis("")
        self.Delete_Profile.setAutoFillBackground(False)
        self.Delete_Profile.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 15px;\n"
"color:white;\n"
"font: 25 16pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-delete-document-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Delete_Profile.setIcon(icon2)
        self.Delete_Profile.setIconSize(QtCore.QSize(40, 40))
        self.Delete_Profile.setObjectName("Delete_Profile")
        self.Delete_Profile.clicked.connect(self.DeleteAllData)
        self.GetData(self.pid)
        self.GenderLine.setReadOnly(True)
        self.fullnameLine.setReadOnly(True)
        self.dateodbirthLine.setReadOnly(True)
        self.departmentLine.setReadOnly(True)
        self.UpdateProfile.clicked.connect(self.UpdateData)
        self.UploadPicture.clicked.connect(self.openImage)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", f"Teacher Screen of {self.pid}"))
        self.address.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Address</span></p></body></html>"))
        self.gender.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Gender</span></p></body></html>"))
        self.UpdateProfile.setText(_translate("Dialog", "UPDATE PROFILE"))
        self.UploadPicture.setText(_translate("Dialog", "Re-Upload Picture"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Department</span></p></body></html>"))
        self.email_id_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email-ID</span></p></body></html>"))
        self.phone_number_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        self.dateofbirth_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Date Of Birth</span></p></body></html>"))
        self.full_name.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.password_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.EditWeclomeLabel.setText(_translate("Dialog", f"Profile of {self.pid}"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Experience</span></p></body></html>"))
        self.Qulaification.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Qualification</span></p></body></html>"))
        self.Delete_Profile.setText(_translate("Dialog", "DELETE PROFILE"))
    
    def DeleteAllData(self):
        
        host="localhost"
        port=3306;dbname="studentDBMS";user="root";password1="reuben"
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        cursor=conn.cursor()

        QueryToGetData1="DELETE FROM studentDBMS.teaches WHERE fac_id=%s;"
        cursor.execute(QueryToGetData1,(self.pid))
        QueryToGetData2="DELETE FROM studentDBMS.faculty WHERE fac_id=%s"
        cursor.execute(QueryToGetData2,(self.pid))

        conn.commit()
        conn.close()
        self.messagebox("Account Deleted",f"{self.pid} is Deleted")

    def convertToBinaryData(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def openImage(self):
        global strimg
        self.url=QFileDialog.getOpenFileName()
        strimg=str(self.url[0])
        self.ImageLabel.setPixmap(QtGui.QPixmap(strimg)) 
    def UpdateData(self):
        global strimg
        global urlofImage
        PID=self.pid
        passwordIn=self.password.text()
        addressIn=self.AddressLine.toPlainText()
        phNumberIn=self.phone_numberline.text()
        emailidIn=self.email_idline.text()
        experIn=self.Experi_InLine.currentText()
        QualIn=self.Qualif_In_Line.currentText()
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
            urlofImage=self.convertToBinaryData(strimg)
        except Exception as err:
            self.warning("ERROR",f"{err} OR FACULTY DOESNT Exist")
        updateargs=(addressIn,passwordIn,phNumberIn,emailidIn,experIn,QualIn,dt_string,urlofImage,PID)
        
        QueryToGetData="UPDATE studentDBMS.faculty set address=%s,passwd=%s,phone_no=%s,email_id=%s,experience=%s,qualification=%s,login_date_time=%s,profile_picture=%s where fac_id=%s"
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
        QueryToGetData="SELECT * FROM studentDBMS.faculty where fac_id=%s"
        cursor.execute(QueryToGetData,PID)
        records=cursor.fetchall()
        # print(records)

        self.fullnameLine.setText(_translate("Dialog",f"{records[0][5]}"))
        self.email_idline.setText(_translate("Dialog",f"{records[0][9]}"))
        self.dateodbirthLine.setText(_translate("Dialog",f"{records[0][4]}"))
        self.GenderLine.setText(_translate("Dialog",f"{records[0][8]}"))
        self.phone_numberline.setText(_translate("Dialog",f"{records[0][7]}"))
        self.password.setText(_translate("Dialog",f"{records[0][1]}"))
        self.departmentLine.setText(_translate("Dialog",f"{records[0][2]}"))
        self.AddressLine.setText(_translate("Dialog",f"{records[0][6]}"))

        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        print("connection successful")
        cursor=conn.cursor()
        query = "SELECT dept_id FROM studentdbms.department;"
        cursor.execute(query)
        result=cursor.fetchall()
        
        for i in range(4):
            self.Qualif_In_Line.addItem("")
        self.Qualif_In_Line.setItemText(0,_translate("Dialog",f"{records[0][3]}"))
        self.Qualif_In_Line.setItemText(1, _translate("AdminScreen", "Bachelor of Engineering "))
        self.Qualif_In_Line.setItemText(2, _translate("AdminScreen", "Master of Engineering "))
        self.Qualif_In_Line.setItemText(3, _translate("AdminScreen", "PhD in Engineering"))

        for i in range(8):
            self.Experi_InLine.addItem("")
        self.Experi_InLine.setItemText(0,_translate("Dialog",f"{records[0][10]}"))
        self.Experi_InLine.setItemText(1, _translate("AdminScreen", "1 Year"))
        self.Experi_InLine.setItemText(2, _translate("AdminScreen", "2 Years"))
        self.Experi_InLine.setItemText(3, _translate("AdminScreen", "3 Years"))
        self.Experi_InLine.setItemText(4, _translate("AdminScreen", "4 Years"))
        self.Experi_InLine.setItemText(5, _translate("AdminScreen", "5 Years"))
        self.Experi_InLine.setItemText(6, _translate("AdminScreen", "More Than 5 Years"))
        self.Experi_InLine.setItemText(7, _translate("AdminScreen", "More Than 10 Years"))
        try:

            # print(str(records[0][13]))
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(records[0][13])
            self.ImageLabel.setPixmap(QtGui.QPixmap(pixmap))
        except Exception as e:
            pass
        conn.commit()
        conn.close()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogTeacher(210029)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
