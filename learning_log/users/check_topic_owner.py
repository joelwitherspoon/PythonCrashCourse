# -*- coding: utf-8 -*-
"""
Check Topic owner. Ch 19 -3 Refactoring

@author: joel
"""
from django.http import Http404

def check_topic_owner(owner, user):
    """Check is the current logged in user is the topic owner"""
    
    if owner != user:
        return Http404



