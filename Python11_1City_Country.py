# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 09:30:21 2020

@author: joel
"""


def city_country(city,country,pop = ''):
    """write a function that accepts a city and country"""
    if pop:
        citycountry = city+', '+country+'-'+pop
    else:
        citycountry = city+', '+country
    return citycountry.title()