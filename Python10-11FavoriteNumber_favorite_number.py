# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 08:44:02 2020
Python 10-11 Favorite Number
@author: joel
"""



import get_favorite_number 
import set_favorite_number
 
def fave():
     """get the favorite number"""
     favenumber = set_favorite_number.set_fave()
     if favenumber:
         print("I know your favorite number! It's \""+favenumber+"\"")
     else:
         favenumber = get_favorite_number.get_fave()
         print("We'll remember it next time!")
         
         