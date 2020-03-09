# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:48:18 2020

@author: jwitherspoon
"""

def make_shirt(size='L',message='I Love Python'):
    
    if size in ['L','M']:
        print("\nYour shirt size is "+ size + " with the message 'I Love Python'")
    else:
        print("\nYour shirt size is "+ size + " with the message '"+message+"'")