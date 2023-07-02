
from django.contrib import admin
from App import views
from django.urls import path

urlpatterns = [
    path('about/', views.about,name="home"),
    path('register/mentor/',views.register_mentee,name="regsiter_mentee"),

 
    
]