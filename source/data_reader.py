welcome_greeting_arr = []
latecomers_greeting_arr = []
invalid_qr_arr= []

with open("data/welcome-greetings-data.txt") as file_in:
    lines = []
    for line in file_in:
        welcome_greeting_arr.append(line.strip())

with open("data/latecomers-greetings-data.txt") as file_in:
    lines = []
    for line in file_in:
        latecomers_greeting_arr.append(line.strip())

with open("data/invalid-qr-data.txt") as file_in:
    lines = []
    for line in file_in:
        latecomers_greeting_arr.append(line.strip())
