# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:00:35 2019

@author: jwitherspoon
"""

aliens =[]
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
    
    #show the first 5 aliens
    for alien in aliens[:5]:
        print(alien)
    print("...")
    
    #show how many aliens have been created.
    print("Total number of aliens: " +str(len(aliens)))