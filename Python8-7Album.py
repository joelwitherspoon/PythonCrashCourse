# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:15:19 2020

@author: jwitherspoon
"""

def make_album(artistname,artisttitle,tracks=''):
    
    if tracks:
        album = {'artisname':artistname,'artisttitle':artisttitle,'tracks':tracks}
    else:
        album = {'artisname':artistname,'artisttitle':artisttitle}        
    
    print(album)
    