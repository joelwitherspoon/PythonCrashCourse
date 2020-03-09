# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:43:16 2020

@author: jwitherspoon
"""

def make_album(artistname,artisttitle,tracks=''):
    
    if tracks:
        album = {'artisname':artistname,'artisttitle':artisttitle,'tracks':tracks}
    else:
        album = {'artisname':artistname,'artisttitle':artisttitle}        
    
    return album
    
while True:
    print("\nPlease enter your album:")
    print("(enter 'q'at any time to quit)")
    
    q_artist = input("Artist name: ")
    if q_artist == 'q':
        break
    
    q_album = input("Album name: ")
    if q_album == 'q':
        break
    
    q_tracks = input("Number of tracks: ")
    if q_tracks == 'q':
        break
    
    collection = make_album(q_artist,q_album,q_tracks)
    print("\n")
    print(collection)
    