# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:08:26 2020

@author: joel
"""


def addition(n1,n2):
    
    try:
       added = int(n1) + int(n2)
    except NameError:
        print("One of your entries is not a number")       
   # except ValueError:
    #    print("One of your entries is not a number")
    else:
        print("Your sum is "+str(added))