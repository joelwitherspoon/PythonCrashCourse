# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:33:40 2020

@author: jwitherspoon
"""

prompt = "\nPlease enter the topping of choice"
prompt += "\n Enter 'quit' to end the program. "

active = True
while active:
    message=input(prompt)
    
    if message != 'quit':
        print("\nWe'll put " + message + " on your pizza.")
    else:
        active = False
        