# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:55:44 2020

@author: jwitherspoon
"""

cities = {
    'Orlando':{
        'country':'united states',
        'population': '2,309,831',
        'fact': 'Home of Disney World'
        },
    
    'Mansfield':{
        'country':'united states',
        'population': '125,000',
        'fact':'Only 5,000 school students'
        },
    
    'Samarkand':{
        'country': 'uzbekistan',
        'population':'950,000',
        'fact': 'My favorite symbol'
        }
    }

for city, city_info in cities.items():
    print("\nCity: "+city)
    countryfrom = city_info['country']
    populationof = city_info['population']
    factof = city_info['fact']
    
    print("\t   Country: " + countryfrom.title())
    print("\tPopulation: " + populationof.title())
    print("\t  Fun fact: " + factof.title())
    
