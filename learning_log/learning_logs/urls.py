# -*- coding: utf-8 -*-
"""URLs for Learning Logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('',views.index,name='index'),
    
    #Show all topics
    path('topics/',views.topics,name='topics'),
    
    #Show topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    #Form for adding a new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    
    #Form for adding a new log entry
    path('new_entry/<int:topic_id>',views.new_entry, name='new_entry')
    
    

]
