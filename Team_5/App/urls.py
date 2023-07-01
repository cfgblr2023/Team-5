
from django.contrib import admin
from Home import views

urlpatterns = [
    path('/', views.home,name="home"),
 
    
]