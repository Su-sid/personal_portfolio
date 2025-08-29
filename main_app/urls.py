from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page

from main_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contact, name='contacts'),
    # Cache projects and resume pages for 1 hour (3600 seconds)
    path('projects', cache_page(3600)(views.projects), name='projects'),
    path('resume', cache_page(3600)(views.resume), name='resume'),
]
