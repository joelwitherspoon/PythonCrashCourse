# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 15:32:22 2020

@author: jwitherspoon
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a random walk and plot the points
rw = RandomWalk(10000)
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15,c=rw.x_values, cmap=plt.cm.nipy_spectral, edgecolor='none')
plt.savefig('RandomWalk1.png',bbox_inches='tight')
