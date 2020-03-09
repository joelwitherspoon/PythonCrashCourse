# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:18:01 2020

@author: jwitherspoon
"""

seating = input("How many people are in the dinner group: ")
seating = int(seating)

if seating > 8:
    print("\nYou'll have to wait for a table.")
else:
    print("\nYour table is ready.")

