# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstScreenrtgJRY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
 ## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from tkinter.constants import FALSE, TRUE
from typing import KeysView
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
import sys
import mysql.connector
import cv2
from mysql.connector.pooling import MySQLConnectionPool
import numpy as np
from PySide2.QtWidgets import *
from pyttsx3 import engine, speak,voice
import speech_recognition as sr
import pyttsx3

#import  facerecognition 


#############################################################################
############   Mainthread class is created for playing  audio ###############
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        self.result=True
    def run(self):
        print("activatejarvish function")
        self.activateJarvish()

    def activateJarvish(self):
        print("activatejarvish function")
        speak("Welcome to jarvish world")
        speak("I am your voice assistent") 
        speak("I am here to assist you to use this app easily")
        i=1
        print(self.result)
        while self.result:
            
            print("activatejarvish function")
          
            #self.jarvishmsg.setText(QCoreApplication.translate("MainWindow", u"Welcome jarvish world", None))
            i=i+1
            speak("if you already have an acount clicked on login button") 
            speak("or click on creat button to create new account")
            if i==4:
                break
            
        
    def speak(audio):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        engine.say(audio)
        engine.runAndWait(1) 

executeThread=MainThread()         

##################################################################################
########################## Main window class for gui and face detection###########
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 551))
        self.widget.setStyleSheet(u"background-color:rgb(0, 0, 0);\n""")     

       

        self.roboRound18 = QLabel(self.widget)
        self.roboRound18.setObjectName(u"roboRound18")
        self.movie=QtGui.QMovie(u"../../Whatsapp media/18.gif")
        self.roboRound18.setMovie(self.movie)
        self.roboRound18.setGeometry(QRect(300, 60, 441, 321))
        self.roboRound18.setAutoFillBackground(True)
        self.roboRound18.setScaledContents(True)
        self.movie.start()

        self.radio8 = QLabel(self.widget)
        self.radio8.setObjectName(u"radio8")
        self.radio8.setGeometry(QRect(50, 50, 201, 371))
        self.movie=QtGui.QMovie(u"../../Whatsapp media/8.gif")
        self.radio8.setMovie(self.movie)
        self.radio8.setScaledContents(True)
        self.movie.start()

        self.jarvishmsg = QLabel(self.widget)
        self.jarvishmsg.setObjectName(u"jarvishmsg")
        self.jarvishmsg.setGeometry(QRect(80, 420, 181, 31))
        self.jarvishmsg.setStyleSheet(u"font: 75 8pt \"Berlin Sans FB\";\n"
"color:rgb(255, 255, 255);")
        self.createbtn = QPushButton(self.widget)
        self.createbtn.setObjectName(u"createbtn")
        self.createbtn.setGeometry(QRect(490, 500, 131, 31))
        self.createbtn.setStyleSheet(u"background-color:rgb(88, 200, 193);\n"
"font: 75 16pt \"Berlin Sans FB\";\n"
"color:rgb(31, 94, 46);")
        self.createbtn.clicked.connect(self.createUser)


        self.loginbtn = QPushButton(self.widget)
        self.loginbtn.setObjectName(u"loginbtn")
        # self.title="Toast"
        # self.message="login button is clicked"
        self.loginbtn.setGeometry(QRect(620, 500, 131, 31))
        self.loginbtn.setStyleSheet(u"background-color:rgb(88, 200, 193);\n"
"font: 75 16pt \"Berlin Sans FB\";\n"
"color:rgb(186, 62, 20);")
        self.loginbtn.clicked.connect(self.detect_face)


        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        executeThread.start()

    # def startTask(self):
       
    #     executeThread.result=True
    #     self.destroyAllWindows()
    #     executeThread.start()
     
      

        
     #print(voices[0].id)
    # setupUi
   

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.roboRound18.setText("")
        self.radio8.setText("")
        
        self.jarvishmsg.setText(QCoreApplication.translate("MainWindow", u"Welcome jarvish world", None))
        self.createbtn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.loginbtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        
    # retranslateUi

    def createUser(self):

        executeThread.result=False
        import facerecognition

    
    def detect_face(self):
        executeThread.result=False
        self.run=True 
        self.name=""
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coords = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
                id,pred = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int(100*(1-pred/300))
                    
                
                mydb=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="Face_authorized_user"
                )
                mycursor=mydb.cursor()
                mycursor.execute("select name from my_table where id="+str(id))
                s = mycursor.fetchone()
                print(s)
                s = ''+''.join(s)
                
                if confidence>80:
                    print(s)
                    self.run=False
                    self.name=s
                    cv2.putText(img,s,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
                    
                else:
                    self.name="UNKNOWN"
                    cv2.putText(img,"UNKNOWN",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)
                
        def recognize(img,clf,faceCascade):
            coords = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture =  cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
        while self.run:
            ret,img = video_capture.read()
            img=  recognize(img,clf,faceCascade)
            cv2.imshow("face detection",img)

            if cv2.waitKey(1)==13:
                break
        if self.run==False:
            
            video_capture.release()
            # self.showDialog
            cv2.destroyAllWindows()
            
            # self.jarvishWindow=Main(self)
            # self.jarvishWindow.show()
            print("user name if "+self.name)
        else:    
            video_capture.release()
            cv2.destroyAllWindows()
    def switchfile(self):
        print("user name swithf"+self.name)
        self.close()	
        
        

    def showDialog(self):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Login")
            msgBox.setWindowTitle("QMessageBox Example")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   

            
 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    # ex.activateJarvishvoice()
    sys.exit(app.exec_())