# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:06:47 2020

@author: jwitherspoon
"""
from die import Die
import pygal
import datetime

#create a D6
die1 = Die()
die2 = Die()

#make some rolls and store rolls in list

results = [die1.roll() + die2.roll() for roll_num in range(50000)]

#analyze the results
max_result = die1.num_sides + die2.num_sides   
frequencies = [results.count(value) for value in range(2,max_result+1)]

currenttime =    str(datetime.time.hour)
#visualize the results
hist = pygal.Bar()
#hist.x_labels1 = [frequency for value in range(3,max_result+1)]
hist.title = "Results of rolling on two D6 50,000 times"
hist.x_labels = [value for value in range(2,max_result+1)]
hist.x_title = "Result "+currenttime
hist.y_title = "Frequency of the result"

hist.add('D6 + D6\n',frequencies)

hist.render_to_file('dices18_visual.svg')
    

