import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Reading Sitka
infile_sitka = open('sitka_weather_2018_simple.csv', 'r')
csvfile_sitka = csv.reader(infile_sitka)
header_row_sitka = next(csvfile_sitka)


# Lists for Sitka
highs_sitka= [] 
lows_sitka=[] 
dates_sitka =[]

# Looping through Sitka
for row in csvfile_sitka:
    try:
        high = int(row[header_row_sitka.index('TMAX')])
        low = int(row[header_row_sitka.index('TMIN')])
        thedate = datetime.strptime(row[header_row_sitka.index('DATE')], '%Y-%m-%d')
        station_sitka = row[header_row_sitka.index('NAME')]
    
    except ValueError:
        pass

    else:
        highs_sitka.append(high)
        lows_sitka.append(low)
        dates_sitka.append(thedate)

# Reading Death Valley
infile_death_valley = open('death_valley_2018_simple.csv', 'r')
csvfile_death_valley = csv.reader(infile_death_valley)
header_row_death_valley = next(csvfile_death_valley)

# Lists for Death Valley
highs_death_valley= [] 
lows_death_valley =[] 
dates_death_valley =[]

# Looping through Death Valley
for row in csvfile_death_valley:
    try:
        high = int(row[header_row_death_valley.index('TMAX')])
        low = int(row[header_row_death_valley.index('TMIN')])
        thedate = datetime.strptime(row[header_row_death_valley.index('DATE')], '%Y-%m-%d')
        station_death_valley = row[header_row_sitka.index('NAME')]
    
    except ValueError:
        pass

    else:
        highs_death_valley.append(high)
        lows_death_valley.append(low)
        dates_death_valley.append(thedate)


fig = plt.figure()

plt.suptitle(f"Temperature comparison between {station_sitka} and {station_death_valley}", fontsize = 16)

# Plotting graph for Sitka
plt.subplot(2,1,1)
plt.plot(dates_sitka, highs_sitka, c='red', alpha = 0.5)
plt.plot(dates_sitka, lows_sitka, c='blue', alpha = 0.5) 
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha = 0.1)

plt.title(station_sitka)

# Plotting graph for Death Valley
plt.subplot(2,1,2)
plt.plot(dates_death_valley, highs_death_valley, c='red', alpha = 0.5)
plt.plot(dates_death_valley, lows_death_valley, c='blue', alpha = 0.5) 
plt.fill_between(dates_death_valley, highs_death_valley, lows_death_valley, facecolor='blue', alpha = 0.1)

plt.title(station_death_valley)

fig.autofmt_xdate()
plt.show()