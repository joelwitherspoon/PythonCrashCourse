# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:15:48 2020

@author: jwitherspoon
"""

sandwich_orders = ['dagwood','blt','pastrami','club']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print("\nI made your "+current_sandwich+" sandwich")
    finished_sandwiches.append(current_sandwich)
    
print("\n--- Sandwich Results ---")   
print("These are the finished sandwiches: \n")
for sandwiches in finished_sandwiches:
    print(sandwiches.title()+"\n")
    

