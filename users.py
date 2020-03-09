# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:04:14 2019

@author: jwitherspoon
"""

users= {
        'aeinstein':{
            'first': 'albert',
            'last' : 'einstein',
            'location':'princeton',
            },
        'mcurie':{
            'first':'marie',
            'last':'curie',
            'location':'paris',
            },
        }
for username, user_info in users.items():
    print("\nUsername: "+ username)
    full_name=user_info['first'] + " "+user_info['last']
    location = user_info['location']
    
    print("\tFull name: "+ full_name.title())
    print("\tLocation: "+location.title())