# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:58:00 2019

@author: jwitherspoon
"""

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print(" - "+topping)
    