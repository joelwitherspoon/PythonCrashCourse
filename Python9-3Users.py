# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 08:35:10 2020

@author: joel
"""


class User():
    """A simple user class"""
    
    def __init__(self,first_name,last_name,location,title,cube_office):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.title = title
        self.cube_office = cube_office
        self.login_attempts 
        
    def describe_user(self):
        print("\nFirst Name: " + self.first_name)
        print("\nLast Name: " + self.last_name)
        print("\nLocation: " + self.location)
        print("\nTitle: " + self.title)
        print("\nCubicle or Office: " + self.cube_office)
        
    def greet_user(self):
        print("\nHello "+self.first_name.title()+" "+self.last_name.title())