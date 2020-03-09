# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:30:28 2020

@author: joel
"""


filename = 'guest.txt'

registration = input("Please enter your name:  ")
with open(filename,'a') as file_object:
    file_object.write(registration)
    file_object.write("\n")
    print(registration)