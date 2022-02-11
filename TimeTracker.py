#!/usr/bin/env python3

import time
from datetime import datetime, date
import csv
import os

# directory of script
script_dir = os.path.dirname(os.path.realpath(__file__))

today = date.today()
current_date = today.strftime("%d.%m.%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


startsignal = input(f"Today is {current_date} and it is {current_time}. To track the time, please type in 'start'.")


if startsignal == "start".lower():
    start = time.time()
    while True:
        endsignal =input("Time is running. If you want to stop the time, type in 'end'.")
        if endsignal == "end".lower():
            end = time.time()
            updated_date = date.today()
            updated_date_form = updated_date.strftime("%d.%m.%Y")
            updated_time = datetime.now()
            updated_time_form = updated_time.strftime("%H:%M:%S")
            hours = (end-start)/3600

            print(f"It took you {end-start} seconds and {hours} hours! Now it is {updated_date_form} and it is {updated_time_form}.")

            DateTime = [current_date, hours]

# Store data as csv
            rows = []
            try:
               # with open('/Users/rea/Documents/TimeTrackerApp/Data.csv', encoding ='utf-8') as e:
               with open(os.path.join(script_dir, "Data.csv"), encoding = 'utf-8') as e:
                    reader = csv.reader(e)
                    for row in reader:
                        rows.append(row)
                    

                    if rows[-1][0] == DateTime[0]:
                        # addierte Zeit für current date
                        newtime = float(rows[-1][1]) + hours

                        # letzten Zeileneintrag löschen
                        rows.pop()
                        rows.append([current_date, newtime])
                        
                        # csv-Datei clearen
                        olddatafile = open(os.path.join(script_dir, "Data.csv"), 'w')
                        olddatafile.truncate()
                        olddatafile.close()

                        # csv-Datei neu beschreiben, mit allen Zeilen 

                        with open(os.path.join(script_dir, "Data.csv"), 'a', encoding='utf-8') as f:
                            writer = csv.writer(f)

                            for row in rows:
                                writer.writerow(row)
                    else:
                        with open(os.path.join(script_dir, "Data.csv"), 'a', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            writer.writerow(DateTime)

                            

            except:
                with open(os.path.join(script_dir, "Data.csv"), 'a', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(DateTime)
            break