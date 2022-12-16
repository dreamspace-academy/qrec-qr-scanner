import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import cv2
import random
import pyttsx3

# Important Variables
camera_id = 0
qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

# Create voice object
def initalize_pyttsx3():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

# Connect with FireStore
def connect_with_firestore():
    credentials_firestore = credentials.Certificate(r"credentials/firebase-auth-file.json")
    credentials_firestore_app = firebase_admin.initialize_app(credentials_firestore)
    firestore_database = firestore.client()    

# Convert text to speech function.
def talk_function(text_data):
    engine.say(text_data)
    engine.runAndWait()

# Current time return function
def get_current_time_data():
    current_date_and_time = datetime.now()
    current_time = current_date_and_time.strftime("%H:%M:%S")
    current_date = current_date_and_time.strftime("%Y-%m-%d")
    current_hour = current_date_and_time.strftime("%H")

    return {"current_time":current_date, "current_date":current_date, "current_hour":current_hour}


def scanner_function():

    while True:
         ret, frame = cap.read()
         
         
         cv2.imshow('Input', frame)
         c = cv2.waitKey(1)
         
         if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()




if __name__=='__main__':
    initalize_pyttsx3()
    connect_with_firestore()
    scanner_function()
