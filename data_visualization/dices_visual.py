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
die3 = Die()

#make some rolls and store rolls in list
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling on D6 and D10 50,000 times"
hist.x_labels = ['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
hist.x_title = "Result"
hist.y_title = "Frequency of the result"

hist.add('D6 + D6\n + D6',frequencies)
hist.render_to_file('dices18_visual.svg')
    
    
