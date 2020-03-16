# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:18:45 2020

@author: jwitherspoon
"""

import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle

filename = 'population_data.json'
with open(filename,encoding="utf8") as f_obj:
    pop_data = json.load(f_obj)
    

#Build a dictionary of population data
            
cc_population = {}
        

#Print the 2010 population for each country    
for pop_dict in pop_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        
        if code:
            print(code+ ": "+str(population))
        else:
            print ('ERROR - '+country_name)

        if code:
            cc_population[code]= population

#Group the countries into 3 population levels
cc_pops1,cc_pops2,cc_pops3,cc_pops4 = {},{},{},{}
for cc, pops in cc_population.items():
    if pops < 10000000:
        cc_pops1[cc] = pops
    elif 10000001 <= pops <= 100000000:
        cc_pops2[cc] = pops        
    elif 100000001 <= pops < 1000000000:
        cc_pops3[cc] = pops
    else:
        cc_pops4[cc] = pops

#Plot the map         
wm_style = RotateStyle('#990099')
wm = World(style=wm_style)
wm.title = 'World population in 2010, by Country'
wm.add('0-10m',cc_pops1)
wm.add('10m-100m',cc_pops2)
wm.add('100m-1bn',cc_pops3)
wm.add('>1bn',cc_pops4)
wm.render_to_file('world_population_b.svg')   

