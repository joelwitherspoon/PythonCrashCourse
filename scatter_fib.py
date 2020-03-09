# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:22:12 2020

@author: jwitherspoon
"""

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

x2_values = list(range(1,1001))
y2_values = [x**1.75 for x in x_values]
plt.scatter(x_values, y_values, s= 40,c='red',edgecolor='blue')



#Set chart title and lable axes.
plt.title("Fibonacci Numbers", fontsize = 24)
plt.xlabel("Value", fontsize= 14)
plt.ylabel("Sequence",fontsize=14)

#set the range for the axis
plt.axis([0,1100,0,1100000])
plt.show()