# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 09:28:01 2020

@author: jwitherspoon
"""

def make_great(magician_in,magician_out):
    
    while magician_in:
        magician_copy = magician_in.pop()
        magician_out.append(magician_copy)
    
    
def show_magicians(magician_outs):
    for name in magician_outs:
        msg = name.title()
        print(msg)    