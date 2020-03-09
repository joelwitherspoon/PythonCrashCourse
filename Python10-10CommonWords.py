# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:53:48 2020

@author: jwitherspoon
"""
def Common_Words(filename,word):
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry the "+filename+" does not exist."
        print(msg)
    else:
        totalcount = contents.lower().count(word)
        print(filename+" has "+str(totalcount)+" counts of the word \""+word+"\"")
