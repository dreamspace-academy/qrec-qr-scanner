import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import cv2
import random
import pyttsx3


engine = pyttsx3.init()
# Use a service account.
cred = credentials.Certificate(r'C:\Users\User\Desktop\qrec\0-qr-scanner\2-final-project\acc.json')

# time setting 
now = datetime.now()
timeN = str(datetime.now())
timeNN = timeN.split(" ")[0]

camera_id = 0
delay = 1
window_name = 'qRec'
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
app = firebase_admin.initialize_app(cred)

db = firestore.client()

current_time = now.strftime("%H:%M:%S")
time = now.strftime("%H")

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

                    staff_ref = db.collection(u'staffs')
                    staff_query = staff_ref.where(u'staff', u'==', str(s)).get()
                   
                    if (staff_query == [] ):
                        engine.say("Hello! This QR code is not valid")
                        engine.runAndWait()
                    else:

                        name = staff_query[0].to_dict()['fname']
                        id = staff_query[0].to_dict()['staff']
                        department = staff_query[0].to_dict()['department']
                        print(name) 
                        if (int(time) < 13):
                            engine.say("Hello!" + str(name) + "Good Morning!!")
                            engine.runAndWait()
                        elif (int(time)> 13):
                            engine.say("Hello!" + str(name) + "Why did you late today?")
                            engine.runAndWait()
                        # Input attendance 
                       
                        doc_ref = db.collection(u'attendance').document(timeNN + " "+ str(name))
                        doc_ref.set({
                            u'name':str(name),
                            u'present':True,
                            u'time': current_time,
                            u'StaffID': id,
                            u'department':department,
                            u'Date':timeNN
                        })              
                        

                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)     
     
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)


