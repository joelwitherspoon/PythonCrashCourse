# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:40:00 2020

@author: jwitherspoon
"""

unconfirmed_users = ['alice','bob','carol','ted']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
    #Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
        