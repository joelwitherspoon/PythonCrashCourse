# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:00:27 2020
Python 10-11 Favorite Number
@author: joel
"""

import json

def get_fave():
    """gets the favorite number"""
    try:
        filename = "favenumber.json"
        with open(filename) as f_obj:
            favenumber = json.load(f_obj)
    except FileNotFoundError:
        return None
    else: 
        return favenumber

