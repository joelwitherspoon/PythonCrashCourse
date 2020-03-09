# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:06:47 2020

@author: jwitherspoon
"""
from die import Die
import pygal

#create a D6
die = Die()

#make some rolls and store rolls in list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analyze the results
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling on D6 1,000 times"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of the result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
    
    
