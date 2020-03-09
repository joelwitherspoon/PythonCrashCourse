# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:31:13 2020

@author: jwitherspoon
"""

def make_car(make, model, **feature):
    car = {}
    car['make'] = make
    car['model'] = model
    for key,value in feature.items():
        car[key] = value
    return car
    