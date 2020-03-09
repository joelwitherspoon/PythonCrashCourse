# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 13:32:05 2020

@author: jwitherspoon
"""

ten = input("Please enter a number: ")
ten = int(ten)

if ten % 10 == 0:
    print("\n It's a multiple of ten.")
else:
    print("\n It's not a multiple of ten.")