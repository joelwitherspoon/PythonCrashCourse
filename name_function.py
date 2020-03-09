# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:16:52 2020

@author: joel
"""


def get_formatted_name(first,last,middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first+' '+middle+' '+last
    else:
        full_name = first+' '+last
    return full_name.title()