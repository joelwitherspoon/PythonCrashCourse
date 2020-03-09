# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 08:16:43 2020

@author: jwitherspoon
"""

favorite_places = {
    'John':{
        'place':'Punta Cana, PR',
        },
    'Mary':{
        'place':'Amsterdam, NL',
        },
    'Akim':{
        'place':'Disney World, FL'
        },
    }

for person, favoriteplace in favorite_places.items():
    print("\nPerson: "+ person)
    print("\tFavorite Place: "+ favoriteplace['place'])