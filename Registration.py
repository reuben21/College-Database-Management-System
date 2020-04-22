

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPixmap
import pymysql
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError
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
from requests import get
from AdminScreenMain import Ui_AdminScreen
from TeacherScreen import Ui_AdminScreen as teacherS
from StudentScreenMain import Ui_StudentScreen

class Ui_Registration_Page(object):
       
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

    def sendEmailOtp(self,email,otp):
        client = boto3.client(
            'ses',
            region_name="ap-south-1",
            aws_access_key_id='AKIATSODTD5QC5ESZX5C',
            aws_secret_access_key='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'
        )
        
        Message=f"The One-Time Password For Registration is:-{otp} "
        response = client.send_email(
            Destination={
                'ToAddresses': ['noreply.sdbms@gmail.com', email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': Message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'One-Time Password Verification',
                },
            },
            Source='noreply.sdbms@gmail.com',
            )         
    
    def sendEmailDetails(self,email,otp):
        client = boto3.client(
            'ses',
            region_name="ap-south-1",
            aws_access_key_id='AKIATSODTD5QC5ESZX5C',
            aws_secret_access_key='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'
        )
        
        Message=f"Login Details: \n PID:- {otp[0]} \n Password:- {otp[1]}"
        response = client.send_email(
            Destination={
                'ToAddresses': ['noreply.sdbms@gmail.com', email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data':Message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'PID and Password To Login',
                },
            },
            Source='noreply.sdbms@gmail.com',
            )
        self.messagebox("Details Sent ",f"Your PID has been send To Your Email:{email}")
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
        self.Submit.setToolTip("")
        self.Submit.setWhatsThis("")
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
        self.full_name.setWhatsThis("")
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
        self.dateofbirth_2.setToolTip("")
        self.dateofbirth_2.setWhatsThis("")
        self.dateofbirth_2.setStyleSheet("\n""color:#1e8bc3;\n""border-radius: 15px;\n""font: 75 14pt \"MS Shell Dlg 2\";")
        self.dateofbirth_2.setObjectName("dateofbirth_2")
        self.password = QtWidgets.QLineEdit(Registration_Page)
        self.password.setGeometry(QtCore.QRect(300, 450, 191, 31))
        self.password.setStyleSheet("background-color:white;\n""border-radius:10px;\n""color:#1e8bc3;\n""border: 1px solid #1e8bc3;\n""font: 25 14pt \"Microsoft YaHei UI Light\";\n""")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.address = QtWidgets.QLabel(Registration_Page)
        self.address.setGeometry(QtCore.QRect(130, 170, 65, 19))
        self.address.setToolTip("")
        self.address.setWhatsThis("")
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
      
       # length of password can be chaged 
       # by changing value in range 
        for i in range(6) : 
            OTP += digits[math.floor(random.random() * 10)]         
        otp=OTP
        print(otp)
        # host="reubendbms.csubdeug2c1q.ap-south-1.rds.amazonaws.com"
        # port=3347;dbname="studentDBMS";user="root";password1="reuben21"
        host="localhost";user="root";password1="reuben";dbname="studentDBMS"
        conn = pymysql.connect(host, user=user,port=3306,passwd=password1, db=dbname)
        cursor=conn.cursor()
        cursor.execute("Truncate onetime")
        query=("INSERT into onetime""(numbers)""VALUES (%s)")
        c=cursor.execute(query,otp)
        query12="SELECT * FROM studentDBMS.onetime"
        cursor.execute(query12)
        ## fetching all records from the 'cursor' object
        records = cursor.fetchall()
        ## Showing the data
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

                                        self.sendEmailOtp(str(emailidIn),otp)
        

                                        i, okPressed = QInputDialog.getInt(None,"Get integer",f"Enter the OTP sent to Email-ID:{emailidIn}", 1, -2147483647, 2147483647, 1)
                                        if okPressed:
                                            print(i) 
                                            if int(i) in listtemp:
                                                print("Email Verified Successfully")

                                                conn = pymysql.connect(host, user=user,port=3306,passwd=password1, db=dbname)
                                                print("connection successful")
                                                cursor=conn.cursor()
                                                args=(str(fullnameIn),str(addressIn),str(phNumberIn),dobIn,str(genderIn),str(passwordIn),str(emailidIn),str(deptIn),dt_string,str(wp))
                                                # insert_query = "INSERT INTO student_registration(PID,first_name,last_name ,address ,phone_no,birthdate,gender,username ,passwd,email_id,class_id) VALUES('%s, %s, %s, %s, %s );" # queries for inserting values
                                                add_student = ("INSERT INTO student_registration "
                                                                "(full_name,address, phone_no,birthdate,gender, passwd,email_id,id_dept, last_login_time_date,Approval) "
                                                                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
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
                                                cursor2=connagain.cursor()
                                                inputPP=("UPDATE studentDBMS.student_registration SET profile_picture=%s WHERE PID=%s;")
                                                if strimg[-4:]==".jpg":
                                                    uploaded_pic = self.upload_to_aws(f"{strimg}", 'image-bucket21', f"{details[0]}.jpg")
                                                elif strimg[-5:]==".jpeg":
                                                    uploaded_pic = self.upload_to_aws(f"{strimg}", 'image-bucket21', f"{details[0]}.jpeg")
                                                elif strimg[-5:]==".JPG":
                                                    uploaded_pic = self.upload_to_aws(f"{strimg}", 'image-bucket21', f"{details[0]}.JPG")
                                                elif strimg[-4:]==".png":
                                                    uploaded_pic = self.upload_to_aws(f"{strimg}", 'image-bucket21', f"{details[0]}.png")
                                                else:
                                                    self.warning("Image Error","Unsupported Image,use jpeg or png")

                                                inPP=(str(urlofImage),details[0])
                                                cursor2.execute(inputPP,inPP)
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
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminScreen = QtWidgets.QDialog()
    ui = Ui_Registration_Page()
    ui.setupUi(AdminScreen)
    AdminScreen.show()
    sys.exit(app.exec_())