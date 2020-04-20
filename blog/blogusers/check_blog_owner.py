# -*- coding: utf-8 -*-
"""
Check Topic owner. Ch 19 -3 Refactoring

@author: joel
"""
def check_blog_owner(owner, user):
    """Check is the current logged in user is the topic owner"""
    
    if owner != user:
        return Http404
    else:
        pass 


