# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:56:59 2020

@author: jwitherspoon
"""

favorite_number = {
    'John': ['12','1'],
    'Mary': ['16','118','3'],
    'Akim': ['3','6','8','12'],
    }
for person, favorites in favorite_number.items():
    print("\n"+person.title()+"'s favorite number(s) are:")
    for favorite in favorites:
        print("\t" + favorite.title())