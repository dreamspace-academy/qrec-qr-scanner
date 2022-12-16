import cv2
# import pymongo
import time
from datetime import datetime
import pyttsx3
engine = pyttsx3.init()

now = datetime.now()


camera_id = 0
delay = 20
window_name = 'OpenCV QR Code'


qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
#Make a routine 
count =1
while count<3:
    #QR scanner
    while True:
        ret, frame = cap.read()

        if ret:
            ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
            if ret_qr:
                for s, p in zip(decoded_info, points):
                    if s:
                        print(s)
                        color = (0, 255, 0)
                        current_time = now.strftime("%H:%M:%S")
                        print("Current Time =", current_time)
                        engine.say("Hello! Welcome " + str(s) +"to the Software Lab")
                        engine.runAndWait()
                    else:
                        color = (0, 0, 255)
                    frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
            cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)
#import decoded QR Name to server
    # import pymongo
    
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.test

    mydb=client["Attendance"]
    mycol=mydb["Record"]
        
    data={'attendance':s, 'Time':current_time }

    mycol.insert_one(data)
    count=count + 1




