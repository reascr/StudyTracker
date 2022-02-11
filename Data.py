#!/usr/bin/env python3

import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('/Users/rea/Documents/PythonProgramme/Data.csv') as csvfile:
    #convert into list of dictionaries
    Data = list(csv.DictReader(csvfile))

print(Data)
# Problem: Keys unterschiedlich: [{'December 05, 2021': 'December 05, 2021', '0.00022098388936784533': '0.00025349166658189564'}]





# Store Data in DataFrame
#TimeDate = ['Date', 'Time']
#df = pd.read_csv('/Users/rea/Documents/PythonProgramme/Data.csv', names = TimeDate)


# Plot: Date on x-Achsis, Time on y-Achsis

#df.set_index('Date').plot()
#plt.show()