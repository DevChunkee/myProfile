from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('experience', views.experience, name='experiece'),
    path('projects', views.projects, name='projects'),
    path('contacts', views.contacts, name='contacts'),
]