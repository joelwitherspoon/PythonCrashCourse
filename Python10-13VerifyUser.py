# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 14:57:11 2020
Python 10-13 Verify User
@author: joel
"""

import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """PRompt for a new username"""
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    namecheck = input("Is your name \""+username+"\"? y/N ")
    if namecheck == 'y':
        print("Welcome back "+ username+"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " +username+"!")

