from datetime import datetime
import random
import pyttsx3


# Create voice object
def initialize_pyttsx3():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
   
    return engine


# Current time return function
def get_current_time_data():
    current_date_and_time = datetime.now()
    current_hour = current_date_and_time.strftime("%H")

    return current_hour
    


def open_sheet():
    # Variables 
    hour_now = get_current_time_data()
    engine = initialize_pyttsx3()
    if int(hour_now) < 11:
        with open('data\welcome-greetings-data.txt', 'r') as file:
            lines = file.readlines()
            line = random.choice(lines)
            while line:
                    print(line)
                    engine.say(line)
                    engine.runAndWait()
                    line = file.readline()

    elif int(hour_now) > 11:  
        with open('data\latecomers-greetings-data.txt', 'r') as file:
            lines = file.readlines()
            line = random.choice(lines)
            while line:
                print(line)
                engine.say(line)
                engine.runAndWait()
                line = file.readline()
                
