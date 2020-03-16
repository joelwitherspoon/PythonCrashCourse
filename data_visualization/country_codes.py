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
        
    if country_name == 'Arab World':
        return 'ae'
    elif country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Libya':
        return 'ly'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Congo, Rep.':
        return 'cg'
    elif country_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Sub-Saharan Africa':
        return 'eh'
    elif country_name == 'Bolivia':
        return 'bo'

    #if the country wasn't found, return none
    return None

