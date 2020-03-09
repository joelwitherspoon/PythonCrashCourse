# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:42:59 2020

@author: joel
"""


guest = ''
filename = "guest_book.txt"
while guest != 'quit':
    guest = input("Please enter the guests name:  ")
    if guest != "quit":
        with open(filename,'a') as file_object:
            file_object.write(guest)
            file_object.write("\n")
        
