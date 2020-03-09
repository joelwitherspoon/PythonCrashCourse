# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:57:09 2020

@author: jwitherspoon
"""
print("Enter numbers to add. \n Enter 'q' to quit")
    
while True:

    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break
        x = int(x)
        
        y = input("\nGive me another number: ")
        if y == 'q':
            break
        y = int(y)
        
    except NameError:
        print("Yo, give me a number!")
    except ValueError:
        print("Yo, give me a number!")
    else:
        ssum = x + y
        print("Your sum is "+str(ssum))  
