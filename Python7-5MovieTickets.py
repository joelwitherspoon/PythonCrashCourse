# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:54:31 2020

@author: jwitherspoon
"""

prompt = "\nPlease enter your age (type 'quit' to exit): "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    elif int(message) < 3:
        print("\nYour ticket is free.")
        break
    elif 3 <= int(message) <= 12:
        print("\nYour ticket is $10")
        break
    elif int(message) > 12:
        print("\nYour ticket is $15")
        break
