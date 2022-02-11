#!/usr/bin/env python3

import time
import sys
from datetime import datetime, date
import csv
#from csv import reader, writer
import os



today = date.today()
current_date = today.strftime("%B %d, %Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Liste = []

startsignal = input(f"Today is {current_date} and it is {current_time}. To track the time, please type in 'start'.")


if startsignal == "start".lower():
    start = time.time()
    while True:
        endsignal =input("Time is running. If you want to stop the time, type in 'end'.")
        if endsignal == "end".lower():
            end = time.time()
            updated_date = date.today()
            updated_date_form = updated_date.strftime("%B %d, %Y")
            updated_time = datetime.now()
            updated_time_form = updated_time.strftime("%H:%M:%S")
            hours = (end-start)/3600

            print(f"It took you {end-start} seconds and {hours} hours! Now it is {updated_date_form} and it is {updated_time_form}.")

            DateTime = [current_date, hours]
            with open('/Users/rea/Documents/PythonProgramme/Data.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)
                
            with open('/Users/rea/Documents/PythonProgramme/Data.csv', 'r', encoding='utf-8') as g:
                reader = csv.reader(g)
                
                for row in reader:
                    Liste.append(row)
                print(Liste)
                print(Liste[0]) #--> eine row
                print(Liste[-1][0]) #--> Datum
                with open('/Users/rea/Documents/PythonProgramme/Data.csv', 'a', encoding='utf-8') as h:
                    writer = csv.writer(h)
                    if Liste[-1][0] != current_date:
                        writer.writerow(DateTime)
                    else:
                        # Addiere Zeiten
                        newtime = float(Liste[-1][1]) + hours
                        NewDateTime = [current_date, newtime]
                        # Lösche letzte Zeile 
                        with open('/Users/rea/Documents/Pythonprogramme/Data.csv', "r") as i:
                            lines =i.readlines()
                            lines=lines[:-1]
                            with open('/Users/rea/Documents/PythonProgramme/Data.csv', "w") as j:
                                writer = csv.writer(i, delimiter=',')
                                for line in lines:
                                    writer.writerow(line)
                            writer.writerow(NewDateTime)
                
            break

# Problem: current_date soll nur einmal in der Tabelle stehen. Zeit soll aufaddiert werden.