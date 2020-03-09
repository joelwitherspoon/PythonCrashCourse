# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:16:30 2020

@author: jwitherspoon
"""

def build_profile(first,last, **user_info):
    
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    