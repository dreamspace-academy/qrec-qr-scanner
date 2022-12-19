from datetime import datetime
import random
import pyttsx3

# Important Variables
data_path_welcome = 'data\welcome-greetings-data.txt'
data_path_late = 'data\latecomers-greetings-data.txt'

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

#Speech module 
def speech_module(data_path):
    engine = initialize_pyttsx3()

    with open(data_path, 'r') as file:
            lines = file.readlines()
            line = random.choice(lines)
            while line:
                    print(line)
                    engine.say(line)
                    engine.runAndWait()
                    line = file.readline()

def open_sheet(limit_time):
    hour_now = get_current_time_data()
    if int(hour_now) < limit_time:
        speech_module(data_path_welcome)

    elif int(hour_now) > limit_time:  
        speech_module(data_path_late)