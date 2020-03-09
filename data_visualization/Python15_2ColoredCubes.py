# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:31:44 2020

@author: jwitherspoon
"""

import matplotlib.pyplot as plt

cubex_values = [1,2,3,4,5]
cubey_values = [1,8,27,64,125]



xcube_values = list(range(-10,5000))
ycube_values = [x**3 for x in xcube_values]

plt.scatter(xcube_values,ycube_values,s=40,c=xcube_values,cmap=plt.cm.jet)
#plt.scatter(cubex_values,cubey_values,s=100, cmap=plt.cm.jet)
