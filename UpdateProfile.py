

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
class Ui_DialogProfile(object):
    def __init__(self,pid):
        self.pid=pid
        print("PID",self.pid)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(952, 612)
        Dialog.setStyleSheet("background-color:#c5eff7;")
        
        self.GenderLine = QtWidgets.QLineEdit(Dialog)
        self.GenderLine.setGeometry(QtCore.QRect(160, 240, 191, 31))
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
        self.address.setGeometry(QtCore.QRect(377, 176, 71, 20))

        self.address.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.address.setObjectName("address")

        self.fullnameLine = QtWidgets.QLineEdit(Dialog)
        self.fullnameLine.setGeometry(QtCore.QRect(160, 180, 191, 31))
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
        self.fullnameLine.setObjectName("fullnameLine")
        self.gender = QtWidgets.QLabel(Dialog)
        self.gender.setGeometry(QtCore.QRect(20, 240, 71, 19))
        self.gender.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.gender.setObjectName("gender")
        self.UpdateProfile = QtWidgets.QPushButton(Dialog)
        self.UpdateProfile.setGeometry(QtCore.QRect(180, 530, 231, 41))
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
        self.ImageLabel = QtWidgets.QLabel(Dialog)
        self.ImageLabel.setGeometry(QtCore.QRect(787, 16, 81, 121))
        self.ImageLabel.setStyleSheet("background-color:#1e8bc3;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border-radius: 10px;\n"
"color:white;")
        self.ImageLabel.setText("")
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.UploadPicture = QtWidgets.QPushButton(Dialog)
        self.UploadPicture.setGeometry(QtCore.QRect(740, 170, 171, 41))
        self.UploadPicture.setStyleSheet("background-color:#1e8bc3;\n"
"border-radius: 10px;\n"
"color:white;\n"
"font: 25 14pt \"Microsoft YaHei UI Light\";\n"
"border:3px solid white;\n"
"")
        self.UploadPicture.setObjectName("UploadPicture")
        self.UploadPicture.clicked.connect(self.openImage)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 470, 131, 20))
        self.label_9.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.email_id_2 = QtWidgets.QLabel(Dialog)
        self.email_id_2.setGeometry(QtCore.QRect(30, 360, 91, 20))
        self.email_id_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.email_id_2.setObjectName("email_id_2")
        self.phone_number_2 = QtWidgets.QLabel(Dialog)
        self.phone_number_2.setGeometry(QtCore.QRect(20, 300, 131, 19))
        self.phone_number_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.phone_number_2.setObjectName("phone_number_2")
        self.dateofbirth_2 = QtWidgets.QLabel(Dialog)
        self.dateofbirth_2.setGeometry(QtCore.QRect(20, 410, 121, 19))

        self.dateofbirth_2.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirth_2.setObjectName("dateofbirth_2")
        self.full_name = QtWidgets.QLabel(Dialog)
        self.full_name.setGeometry(QtCore.QRect(20, 180, 91, 19))

        self.full_name.setStyleSheet("\n"
"color:#1e8bc3;\n"
"border-radius: 15px;\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.full_name.setObjectName("full_name")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(470, 300, 191, 31))
        self.password.setStyleSheet("background-color:white;\n"
        "border-radius:15px;\n"
        "color:#1e8bc3;\n"
        "border: 1px solid #1e8bc3;\n"
        "font: 25 14pt \"Microsoft YaHei UI Light\";\n"
        "")
        self.password.setObjectName("password")
        self.departmentLine = QtWidgets.QLineEdit(Dialog)
        self.departmentLine.setGeometry(QtCore.QRect(160, 470, 191, 31))
        self.departmentLine.setStyleSheet("background-color:white;\n"
        "border-radius:15px;\n"
        "color:#1e8bc3;\n"
        "border: 1px solid #1e8bc3;\n"
        "font: 25 14pt \"Microsoft YaHei UI Light\";\n"
        "")
        self.departmentLine.setObjectName("departmentLine")
        self.phone_numberline = QtWidgets.QLineEdit(Dialog)
        self.phone_numberline.setGeometry(QtCore.QRect(160, 300, 191, 31))
        self.phone_numberline.setStyleSheet("background-color:white;\n"
        "border-radius:15px;\n"
        "color:#1e8bc3;\n"
        "border: 1px solid #1e8bc3;\n"
        "font: 25 14pt \"Microsoft YaHei UI Light\";\n"
        "")
        self.phone_numberline.setObjectName("phone_numberline")
        self.password_2 = QtWidgets.QLabel(Dialog)
        self.password_2.setGeometry(QtCore.QRect(367, 296, 91, 20))
        self.password_2.setStyleSheet("\n"
        "color:#1e8bc3;\n"
        "border-radius: 15px;\n"
        "font: 75 14pt \"MS Shell Dlg 2\";")
        self.password_2.setObjectName("password_2")
        self.AddressLine = QtWidgets.QTextEdit(Dialog)
        self.AddressLine.setGeometry(QtCore.QRect(470, 180, 191, 91))
        self.AddressLine.setStyleSheet("background-color:white;\n""border-radius:15px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 12pt \"Microsoft YaHei UI Light\";\n""")
        self.AddressLine.setObjectName("AddressLine")

        self.EditWeclomeLabel = QtWidgets.QPushButton(Dialog)
        self.EditWeclomeLabel.setGeometry(QtCore.QRect(210, 10, 491, 51))
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
        self.email_idline.setGeometry(QtCore.QRect(160, 360, 501, 31))
        self.email_idline.setStyleSheet("background-color:white;\n"
        "border-radius:15px;\n"
        "color:#1e8bc3;\n"
        "border: 1px solid #1e8bc3;\n"
        "font: 25 14pt \"Microsoft YaHei UI Light\";\n"
        "")
        self.email_idline.setText("")
        self.email_idline.setObjectName("email_idline")
        self.dateodbirthLine = QtWidgets.QLineEdit(Dialog)
        self.dateodbirthLine.setGeometry(QtCore.QRect(160, 410, 191, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateodbirthLine.sizePolicy().hasHeightForWidth())
        self.dateodbirthLine.setSizePolicy(sizePolicy)
        self.dateodbirthLine.setStyleSheet("background-color:white;\n""border-radius:15px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.dateodbirthLine.setObjectName("dateodbirthLine")

        self.Delete_Profile = QtWidgets.QPushButton(Dialog)
        self.Delete_Profile.setGeometry(QtCore.QRect(460, 530, 231, 41))
        self.Delete_Profile.setMouseTracking(True)
        self.Delete_Profile.setTabletTracking(True)

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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", f"Student Profile of {self.pid}"))
        self.address.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Address</span></p></body></html>"))
        self.gender.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Gender</span></p></body></html>"))
        self.UpdateProfile.setText(_translate("Dialog", "UPDATE PROFILE"))
        self.UploadPicture.setText(_translate("Dialog", "Re-Upload Picture"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Department</span></p></body></html>"))
        self.email_id_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email-ID</span></p></body></html>"))
        self.phone_number_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Phone Number</span></p></body></html>"))
        self.dateofbirth_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Date Of Birth</span></p></body></html>"))
        self.full_name.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.full_name.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Full Name</span></p></body></html>"))
        self.password_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.EditWeclomeLabel.setText(_translate("Dialog", f"Profile of {self.pid}"))
        self.Delete_Profile.setText(_translate("Dialog", "DELETE PROFILE"))
    
    def upload_to_aws(self,local_file, bucket, s3_file):
        ACCESS_KEY = 'AKIATSODTD5QC5ESZX5C'
        SECRET_KEY = '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'
        global urlofImage
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)

        try:
            s3.upload_file(local_file, bucket, s3_file, ExtraArgs={'ACL':'public-read'})
            print("Upload Successful")
            #url-https://image-bucket21.s3.ap-south-1.amazonaws.com/firstimage.png
            urlofImage=f"https://{bucket}.s3.ap-south-1.amazonaws.com/{s3_file}"
            return True
        except FileNotFoundError:
            print("FileNotFoundError","The file was not found")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("The file was not found")
            msg.setWindowTitle("FileNotFoundError")
            msg.exec_()
            return False
        except NoCredentialsError:
            print("NoCredentialsError","Credentials Incorrect")
            msg = QMessageBox()
            msg.setIcon(QIcon('education.ico'))
            msg.setText("Error")
            msg.setInformativeText("TCredentials Incorrect")
            msg.setWindowTitle("NoCredentialsError")
            msg.exec_()
            return False
    def openImage(self):
        global strimg
        self.url=QFileDialog.getOpenFileName()
        strimg=str(self.url[0])
        self.ImageLabel.setPixmap(QtGui.QPixmap(strimg)) 

    def convertToBinaryData(self,filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def UpdateData(self):
        global strimg
        global urlofImage
        PID=self.pid
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
            # print(pp[0][0])
            urlofImage=pp[0][0]
            urlofImage = self.convertToBinaryData(strimg)
        except Exception as Err:
            self.messagebox("Data Not Updated Error:",f"{err}")

        updateargs=(addressIn,passwordIn,phNumberIn,emailidIn,dt_string,urlofImage,PID)
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
        self.fullnameLine.setText(_translate("Dialog",f"{records[0][1]}"))
        self.email_idline.setText(_translate("Dialog",f"{records[0][7]}"))
        self.dateodbirthLine.setText(_translate("Dialog",f"{records[0][4]}"))
        self.GenderLine.setText(_translate("Dialog",f"{records[0][5]}"))
        self.phone_numberline.setText(_translate("Dialog",f"{records[0][3]}"))
        self.password.setText(_translate("Dialog",f"{records[0][6]}"))
        self.departmentLine.setText(_translate("Dialog",f"{records[0][8]}"))
        self.AddressLine.setText(_translate("Dialog",f"{records[0][2]}"))
        print(type(records[0][11]))
        try:

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(records[0][11])
            self.ImageLabel.setPixmap(QtGui.QPixmap(pixmap))
        except Exception as e:
            pass
        conn.commit()
        conn.close()

    def DeleteAllData(self):
        
        host="localhost"
        port=3306;dbname="studentDBMS";user="root";password1="reuben"
        conn = pymysql.connect(host, user=user,port=port,passwd=password1, db=dbname)
        cursor=conn.cursor()
        QueryToGetData="DELETE FROM studentDBMS.exam_scheme WHERE pid=%s"
        cursor.execute(QueryToGetData,(self.pid))
        QueryToGetData1="DELETE FROM studentDBMS.takes WHERE PID=%s;"
        cursor.execute(QueryToGetData1,(self.pid))
        QueryToGetData2="DELETE FROM studentDBMS.student_registration WHERE PID=%s"
        cursor.execute(QueryToGetData2,(self.pid))

        conn.commit()
        conn.close()
        self.messagebox("Account Deleted",f"{self.pid} is Deleted")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogProfile(181034)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
