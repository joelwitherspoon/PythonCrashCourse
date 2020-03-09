# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 08:04:03 2020

@author: joel
"""


filename = 'learning_python.txt'

 
with open(filename) as file_object2:
    lines = file_object2.readlines()

for line in lines: 
    message = line.replace('Python','Java')
    print(message.rstrip())
    