# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:56:57 2020

@author: jwitherspoon
"""

person1 = {
    'firstname':'Loren',
    'lastname':'Witherspoon',
    'age':'54',
    'city':'Bartlesville',
    }
person2 = {
    'firstname':'Leslie',
    'lastname':'Witherspoon',
    'age':'40',
    'city':'Tulsa',
    }
person3 = {
    'firstname':'Rachel',
    'lastname':'Harper',
    'age':'33',
    'city':'Oklahoma City',
    }

People = [person1,person2,person3]

for person in People:
    for k , v in person.items():
        print(person.keys()," :: ",person.values())
       