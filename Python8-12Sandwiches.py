# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 10:40:48 2020

@author: jwitherspoon
"""

def sandwich_items(*items_sandwich):
    print("\nMake a sandwich with these toppings: ")
    for items in items_sandwich:
        print (" - "+items)
        