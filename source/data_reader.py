from datetime import datetime
import random


# Current time return function
def get_current_time_data():
    current_date_and_time = datetime.now()
    current_time = current_date_and_time.strftime("%H:%M:%S")
    current_date = current_date_and_time.strftime("%Y-%m-%d")
    current_hour = current_date_and_time.strftime("%H")

    return [current_time, current_date, current_hour]

greeting_data = open("data/welcome-greetings-data.txt", 'r')

# print(greeting_data)