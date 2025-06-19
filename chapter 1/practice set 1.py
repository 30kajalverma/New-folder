
# problem 1
print('''
      
      Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
      
      ''')
# problem 2 table of 5
#  using python as a calculator
# window + R , THEN cmd , then ok , then write python in terminal and enter then u can calculate any digits for example 12*12 enter 144 
# REPL: READ, EVALUATE, PRINT , LOOP  TO YE BR BR KHEGA AAGE CALCULATION KRNE KO DO


# problem 3

import pyttsx3
engine = pyttsx3.init()
engine.say("HELLOO SANJAY SONI ")
engine.runAndWait()




# PROBLEM 4
import os

# Specify the directory path
directory_path = '/ semester 1'

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)

