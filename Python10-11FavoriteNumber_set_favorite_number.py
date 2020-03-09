# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:44:02 2020
Python 10-11 Favorite Number
@author: joel
"""


import json
 
def set_fave():
     """set the favorite number"""
     number = input("\nWhat is your favmorite number ")
     filename = "favenumber.json"
     with open(filename,'w') as f_obj:
             json.dump(number,f_obj)
     return number