import cv2
import pyttsx3
import firebase_admin
from datetime import datetime
from data_reader import open_sheet
from firebase_admin import firestore
from firebase_admin import credentials


# Important Variables
camera_id = 0
qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
delay = 1
window_name = 'qRec'
limit_time = 11
qr_counter = 0

# Messages 
invalid_msg = "This QR code is not valid"
already_exists_msg = "This QR code exists already!"

# Configuration path
config_path = r"credentials/firebase-auth-file.json"

# Create voice object
def initialize_pyttsx3():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
   
    return engine


# Connect with FireStore
def connect_with_firestore():
    credentials_firestore = credentials.Certificate(config_path)
    firebase_admin.initialize_app(credentials_firestore)
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
   
    
    return [year_only,month_only, date_only]


# Variable for pyttsx3
engine_say = initialize_pyttsx3()


# Define Scanner Function
def scanner_function(database):
    global qr_counter

    while True:
        ret, frame = cap.read()
        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for QrValue, point in zip(decoded_info, points):
                    if QrValue:

                        if qr_counter == 5:

                            #print(f'QR Data: {QrValue}')
                            
                            # Retrieve data for time 
                            time_now, date_now, hour_now = get_current_time_data()
                            
                            staff_ref = database.collection(u'staffs')
                            staff_query = staff_ref.where(u'staff', u'==', str(QrValue)).get()
                            
                            if (staff_query == [] ):
                                engine_say.say (invalid_msg)
                                engine_say.runAndWait()

                            else:
                                attendance_ref = database.collection(u'attendance')
                                attendance_query = attendance_ref.where(u'StaffID', u'==', str(QrValue)).get()
                                if (attendance_query == [] ):
                                    name = staff_query[0].to_dict()['fname']
                                    id = staff_query[0].to_dict()['staff']
                                    department = staff_query[0].to_dict()['department']
                                    print(name) 
                                    if (int(hour_now) < limit_time):
                                        engine_say.say("Hey!"+ str(name))
                                        open_sheet(limit_time)

                                    elif (int(hour_now)>= limit_time):
                                        engine_say.say("Hey!"+ str(name))
                                        open_sheet(limit_time)
                                        
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
                                    print(already_exists_msg)
                                    engine_say.say(already_exists_msg)
                                    engine_say.runAndWait()

                                qr_counter = 0

                        qr_counter = qr_counter + 1 
                    frame = cv2.polylines(frame, [point.astype(int)], True, (255, 0, 0), 4)
            cv2.imshow(window_name, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)

if __name__=='__main__':
    
    database = connect_with_firestore()
    scanner_function(database)
    