
import random

# Open the file in read mode
with open('data\welcome-greetings-data.txt', 'r') as f:
  # Read all the lines of the file into a list 
 lines = f.readlines()

# Use random.choice() to select a random line from the list
line = random.choice(lines)

# Print the random line
print(line)