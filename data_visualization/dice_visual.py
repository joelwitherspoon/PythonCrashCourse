# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:06:47 2020

@author: jwitherspoon
"""
from die import Die
import pygal

#create a D6
die1 = Die()
die2 = Die()

#make some rolls and store rolls in list
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#analyze the results
frequencies = []
max_results = die1.num_sides + die2.num_sides
for value in range(2,max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1,000 times"
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of the result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')
    
    
