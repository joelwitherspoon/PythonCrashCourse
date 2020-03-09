#-*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over")
        
    def how_old(self):
        print(str(self.age) + " months old")