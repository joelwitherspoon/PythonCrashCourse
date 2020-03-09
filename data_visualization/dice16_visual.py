# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:06:47 2020

@author: jwitherspoon
"""
from die import Die
import pygal

#create a D6
die1 = Die()
die10 = Die(10)

#make some rolls and store rolls in list
results = []
for roll_num in range(50000):
    result = die1.roll() + die10.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = die1.num_sides + die10.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling on D6 and D10 50,000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of the result"

hist.add('D6 + D10',frequencies)
hist.render_to_file('dice10_visual.svg')
    
    
