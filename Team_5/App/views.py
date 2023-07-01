from django.shortcuts import render,request

# Create your views here.


def home(request) :
    return render(request,"home.html")
