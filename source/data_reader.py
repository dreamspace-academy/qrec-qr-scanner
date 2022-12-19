import run
import random


greeting_data = []


with open("data/welcome-greetings-data.txt", 'r') as f:
    for line in f:
        greeting_data.append(line)

print(greeting_data)