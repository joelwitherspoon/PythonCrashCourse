# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:03:32 2020

@author: jwitherspoon
"""

Hercules = {
    'kind':'Yorkie',
    'gender':'M',
    'owner': 'JWitherspoon',
    }
Sylvester = {
    'kind': 'Aberline Cat',
    'gender':'F',
    'owner':'LWitherspoon',
    }
Link = {
        'kind':'Teacup Yorkie',
        'gender': 'F',
        'owner':'Kid Fury',
        }
pets = [Hercules,Sylvester,Link]

for pet in pets:
    for k,v, in pet.items():
        print(k,v)
        