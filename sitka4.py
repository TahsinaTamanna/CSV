# handle error checking using try except
# change file to use death_valley data

import csv
import matplotlib.pyplot as plt
from datetime import datetime

infile = open('death_valley_2018_simple.csv', 'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row): # finding index location
    print(index, column_header)

highs =[]
lows = []
dates =[]

for row in csvfile:
    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], '%Y-%m-%d')
    
    except ValueError:
        print(f"Missing data for {row[2]}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)
   

fig = plt.figure()

plt.plot(dates, highs, c='red', alpha = 0.5)

plt.plot(dates, lows, c='blue', alpha = 0.5) 

plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)

plt.title("Daily high and low temp for Sitka Alaska, 2018", fontsize = 16)

plt.xlabel("Dates", fontsize = 12)

plt.ylabel("Temperature(F)", fontsize = 16)

plt.tick_params(axis= "both" , which= "major", labelsize = 10)

fig.autofmt_xdate()

plt.show()