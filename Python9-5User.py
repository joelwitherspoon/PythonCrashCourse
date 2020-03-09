# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:10:42 2020

@author: jwitherspoon
"""

class User():
    def __init__(self,first_name, last_name, account_created, department,\
                 location):
        self.first_name = first_name
        self.last_name = last_name
        self.account_created = account_created
        self.department = department
        self.location = location
        self.login_attempts = 1
        
    def describe_user(self):
        print("\n This is the information on "+self.first_name+" "+self.last_name)
        print("\n Account Created: "+ str(self.account_created))
        print("\n Department: "+self.department)
        print("\n Location: "+self.location)
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("\n Login Attemps: "+str(self.login_attempts))
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("\n Login Attemps: "+str(self.login_attempts))
    
        
    