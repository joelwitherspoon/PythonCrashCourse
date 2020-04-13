"""Defines urls for blog app"""

from django.urls import include, path

from . import views

app_name = 'blogs'
urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    
    #Posts Listing
    path('posts/',views.posts, name='posts'),
    
    #Single post listing
    path('posts/<int:blogpost_id>',views.post, name='post'),
    
    #New entry page
    path('new_post/',views.new_post,name='new_post'),
    
     
    
    ]