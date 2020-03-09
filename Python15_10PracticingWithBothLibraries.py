# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 14:31:31 2020

@author: jwitherspoon
"""

import pygal
from random_walk import RandomWalk

rw1 = RandomWalk()
rw2 = RandomWalk()
rw3 = RandomWalk()
rw1.fill_walk()
rw2.fill_walk()
rw3.fill_walk()
xy1=[i for i in zip(rw1.x_values,rw1.y_values)]
xy2=[i for i in zip(rw2.x_values,rw2.y_values)]
xy3=[i for i in zip(rw3.x_values,rw3.y_values)]
scatter_chart = pygal.XY(stroke = False)
scatter_chart.title = 'Random Walk'
scatter_chart.add('Step1',xy1)
scatter_chart.add('Step2',xy2)
scatter_chart.add('Step3',xy3)


scatter_chart.render_to_file('randomwalk_xy.svg')