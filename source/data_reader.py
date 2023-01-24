welcome_greeting_arr = []
latecomers_greeting_arr = []
invalid_qr_arr= []

with open("C:/Users/User/Desktop/qrec-qr-scanner/source/data/welcome-greetings-data.txt") as file_in:
    lines = []
    for line in file_in:
        welcome_greeting_arr.append(line.strip())

with open("C:/Users/User/Desktop/qrec-qr-scanner/source/data/latecomers-greetings-data.txt") as file_in:
    lines = []
    for line in file_in:
        latecomers_greeting_arr.append(line.strip())

with open("C:/Users/User/Desktop/qrec-qr-scanner/source/data/invalid-qr-data.txt") as file_in:
    lines = []
    for line in file_in:
        invalid_qr_arr.append(line.strip())
