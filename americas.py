# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:19:29 2020

@author: jwitherspoon
"""

from pygal.maps.world import World
wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br', \
                        'cl','co','ec','gf','gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas.svg')

