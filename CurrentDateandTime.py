#!/usr/bin/env python3

import sys
from datetime import datetime, date

today = date.today()
date = today.strftime("%B %d, %Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# sys module provides access to any command-line arguments via sys.argv.
# sys.argv is a list of arguments. sys.arg[0] is always the program/script name

if len(sys.argv) != 2:
    print("Error. Please type in 'start' in order to get the current date and time. Try again!")
    sys.exit()
elif sys.argv[1].lower() == "start":
    print(f"Today is {str(date)} and the current time is {current_time}.")
else:
    print("Error. Please type in 'start' in order to get the current date and time. Try again!")
    sys.exit() 
