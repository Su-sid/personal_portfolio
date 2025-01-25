from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contact, name='contacts'),
    path('projects', views.projects, name='projects'),
    path('resume', views.resume, name='resume'),

]
