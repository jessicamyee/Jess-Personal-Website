"""Defines URL patterns for learning_logs."""

from django.conf.urls import url
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>[0-9]+)/',views.edit_entry, name='edit_entry'),
    #Page for adding a new entry
    url(r'^new_entry/(?P<topic_id>[0-9]+)/', views.new_entry, name='new_entry'),
    #Page for adding a new topic
    url(r'^new_topic/', views.new_topic, name='new_topic'),
    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>[0-9]+)/', views.topic, name='topic'),
    # Show all topics
    url(r'^topics/', views.topics, name = 'topics'),
    # Home page
    url(r'^', views.index, name='index'),

    
]
