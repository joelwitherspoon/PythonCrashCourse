# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:01:49 2020

@author: jwitherspoon
"""

class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\n Name: "+self.restaurant_name+" Cuisine: "+self.cuisine_type)
        
    def open_restaurant(self):
        print("\n"+ self.restaurant_name +" is open")
        
    def set_number_served(self,served):
        self.number_served = served
        print("\n"+str(self.number_served)+" have been served")
    
    def increment_number_served(self,new_patrons):
        self.number_served += new_patrons
        print("\n"+str(self.number_served)+" now have been served")
        
        