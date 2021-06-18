import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib  #This is used to send email
import random
import time
import sys
import re  #Support for regular expressions (RE). Hover mouse cursor over re to learn more about it
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, QTime, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUI


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id) 


# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]


# This is a wish function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This is a wish function, this wishes us accourding to the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hello Sir")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis, your personal assistant. Please tell me how can I help you")

#This function is sends email for us
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sandeepkumarkarmkar49@gmail.com', 'Sandeep749@123')
    server.sendmail('sandeepkumarkarmkar49@gmail.com', to, content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    # It takes microPhone input from user and returns String output
    def takeCommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)

            print("Say that again please...")
            return "None"
        return query


    def TaskExecution(self):
        wishMe()
        while True:
        # if 1:
            self.query = self.takeCommand().lower()

            # logic for executing tasks on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif self.query in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in self.query:
                webbrowser.open("google.com")
            
            elif 'open stackoverflow' in self.query:
                webbrowser.open("stackoverflow.com")
            
            elif 'play music' in self.query or 'play song' in self.query:
                music_dir = 'D:\\songs\\audio'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif re.search('date', self.query):
                """
                Just return date as string
                :return: date if success, False if fail
                """
                try:
                    date = datetime.datetime.now().strftime("%b %d %Y")
                except Exception as e:
                    print(e)
                    date = False
                print(date)
                speak(f"Sir, it's {date} today")

            elif 'the time' in self.query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strtime}")

            elif 'open vs code' in self.query:
                codepath = "C:\\Users\\Pradeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                speak("Opening VS Code sir, please wait, it may take some time")

            elif re.search('launch', self.query):
                dict_app = {
                    'chrome': '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"',
                    'vs code': 'C:\\Users\\Pradeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                }

                app = self.query.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak('Launching: ' + app + 'for you sir!')
                    try:
                        os.startfile(path)
                    except Exception as e:
                        print(e)

            elif 'email to sandeep' in self.query:
                try:
                    speak("what should I say?")
                    content = self.takeCommand()
                    to = "sandeepkarmkar49@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Sandeep bhai, I cannot sent this email")

            elif 'quit' in self.query:
                speak("OK Sir, I am terminating myself in t minus three seconds")
                time.sleep(0.5)
                speak("three")
                time.sleep(1)
                speak("two")
                time.sleep(1)
                speak("one")
                quit()

startExecution = MainThread()


#Any setup related thing is made in this class for the gui window
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/latest_tech_tutorials/jarvishProjecttrail/gif/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("E:/latest_tech_tutorials/jarvishProjecttrail/gif/Jarvis Loading Screen on Make a GIF.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        self.ui.movie = QtGui.QMovie("E:latest_tech_tutorials/jarvishProjecttrail/gif/Iron Man 3 Fan Art_ Iron Man gifs.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)

        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())