# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:48:11 2020

@author: jwitherspoon
"""

file_cats = "cats.txt"
file_dogs = "dogs.txt"
animals = []
try:
    with open (file_cats) as c_obj:
        animals.append(c_obj.readlines())

    with open (file_dogs) as d_obj:
        animals.append(d_obj.readlines())
        
except FileNotFoundError as fnfe:
    #print("The file could not be located")
    print(type(fnfe),fnfe.args,fnfe.value)
else:
    print(animals)
    