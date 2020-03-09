# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:13:48 2020

@author: joel
"""


class Restaurant():
    """Try it yourself Ch 9 ex 1   """ 
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThis is a "+self.cuisine_type.title() + " restaurant named "+
              self.restaurant_name.title())
    
    def open_restaurant(self):
        print(self.restaurant_name.title()+" is open")
        
    def set_number_served(self,customers):
        self.number_served = customers
        
    def increment_number_served(self,customers):
        self.number_served += customers
        print(str(self.number_served)+ " people served today.")
    
        
        