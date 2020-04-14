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
    
    #New post page
    path('new_post/',views.new_post,name='new_post'),
    
    #Edit post
    path('edit_post/<int:blogpost_id>/', views.edit_post, name='edit_post')
    
    
    
    ]