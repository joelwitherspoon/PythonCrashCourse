# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Get dates and temps from file
def get_dates_and_temps(filename, dates,highs,lows):
    """Get the dates, highs, and lows from file"""
    with open(filename) as f_obj:
        reader = csv.reader(f_obj)
        header_row = next(reader)
        
        for column in reader:
            
            try:
                current_date = datetime.strptime(column[0], "%Y-%m-%d")
                high = int(column[1])
                low = int(column[3])
            except ValueError:
                print(current_date,'missing data')
            else:
                dates.append(current_date)                
                highs.append(high)
                lows.append(low)

#plot the figure
fig = plt.figure(dpi=128, figsize=(15,9))
"""#Get the weather data for Sitka
dates, highs, lows = [],[],[]
get_dates_and_temps('sitka_weather_2014.csv', dates, highs, lows)

#plot the data for Sitka        
plt.plot(dates,highs, c='red')
plt.plot(dates,lows, c='blue')
plt.fill_between(dates,highs,lows, facecolor='indigo', alpha=0.9)

#Get the weather data for Death Valley
dates, highs, lows = [],[],[]
get_dates_and_temps('death_valley_2014.csv', dates, highs, lows)

#plot the data for Death Valley
plt.plot(dates,highs, c='red', alpha= 0.5)
plt.plot(dates,lows, c='blue',alpha= 0.5)
plt.fill_between(dates,highs,lows, facecolor='green', alpha=0.5)"""

#Get the weather data for San Francisco
dates, highs, lows = [],[],[]
get_dates_and_temps('san_francisco_2014.csv', dates, highs, lows)

#plot the data for San Francisco
plt.plot(dates,highs, c='red', alpha= 0.3)
plt.plot(dates,lows, c='blue',alpha= 0.3)
plt.fill_between(dates,highs,lows, facecolor='pink', alpha=0.3)
    
#format the plot
title = "Daily High and Low Temperatures in \n"
title += "San Francisco, CA -2014"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.ylim(0, 120)

#plt.savefig('dhltemps_sitka_sanfran_deathvalley.png')
plt.show()