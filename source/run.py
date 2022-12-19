import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import cv2
import data_reader
import pyttsx3
from data_reader import open_sheet


# Create voice object
def initialize_pyttsx3():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
   
    return engine


# Connect with FireStore
def connect_with_firestore():
    credentials_firestore = credentials.Certificate(r"credentials/firebase-auth-file.json")
    credentials_firestore_app = firebase_admin.initialize_app(credentials_firestore)
    firestore_database = firestore.client()    
    return firestore_database


# Current time return function
def get_current_time_data():
    current_date_and_time = datetime.now()
    current_time = current_date_and_time.strftime("%H:%M:%S")
    current_date = current_date_and_time.strftime("%Y-%m-%d")
    current_hour = current_date_and_time.strftime("%H")

    return [current_time, current_date, current_hour]
# Current time return function
def get_date_month_year_only():
    current_date_and_time = datetime.now()
    year_only = current_date_and_time.strftime("%Y")
    month_only = current_date_and_time.strftime("%m")
    date_only = current_date_and_time.strftime("%d")
   
    
    return [ year_only,month_only, date_only]


# Important Variables
camera_id = 0
qcd = cv2.QRCodeDetector()
engine_say = initialize_pyttsx3()
cap = cv2.VideoCapture(camera_id)


# Define Scanner Function
def scanner_function(database):

    camera_id = 0
    delay = 1
    window_name = 'qRec'

    qcd = cv2.QRCodeDetector()
    cap = cv2.VideoCapture(camera_id)

    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                        print(s)
                        color = (0, 255, 0)
                        # Retrieve data 
                        time_now, date_now, hour_now = get_current_time_data()
                        
                        staff_ref = database.collection(u'staffs')
                        staff_query = staff_ref.where(u'staff', u'==', str(s)).get()
                        if (staff_query == [] ):
                            engine_say.say ("This QR code is not valid")
                            engine_say.runAndWait()

                        else:
                            attendance_ref = database.collection(u'attendance')
                            attendance_query = attendance_ref.where(u'StaffID', u'==', str(s)).get()
                            if (attendance_query == [] ):
                                name = staff_query[0].to_dict()['fname']
                                id = staff_query[0].to_dict()['staff']
                                department = staff_query[0].to_dict()['department']
                                print(name) 
                                if (int(hour_now) < 11):
                                    engine_say.say("Hey!"+ str(name))
                                    open_sheet()

                                elif (int(hour_now)>= 11):
                                    engine_say.say("Hey!"+ str(name))
                                    open_sheet()
                                    
                                # Input attendance 
                                year_only, month_only, date_only = get_date_month_year_only()

                                doc_ref = database.collection(u'attendance').document(date_now + " "+ str(name))
                                doc_ref.set({
                                    u'name':str(name),
                                    u'present':True,
                                    u'time': time_now,
                                    u'StaffID': id,
                                    u'department':department,
                                    u'Date':date_now,
                                    u'Year':year_only,
                                    u'Month': month_only,
                                    u'Date_only':date_only
                                    })
                            else:
                                print("This QR code exists already!")
                                engine_say.say("This QR code exists already!")
                                engine_say.runAndWait()
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
            cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)

if __name__=='__main__':
    
    database = connect_with_firestore()
    scanner_function(database)
    