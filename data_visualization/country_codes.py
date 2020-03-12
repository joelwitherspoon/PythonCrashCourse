# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:10:30 2020

@author: jwitherspoon
"""
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return Pygal 2 character country code"""
    
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #if the country wasn't found, return none
    return None

