# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:15:48 2020

@author: jwitherspoon
"""

sandwich_orders = ['dagwood','pastrami','blt','pastrami','club','pastrami']

print("\nThe deli has run out of pastrami sandwiches!")
while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n--- Sandwich Results ---")
print("These are the finished sandwiches: \n")
for sandwiches in sandwich_orders:
    print(sandwiches.title()+"\n")

