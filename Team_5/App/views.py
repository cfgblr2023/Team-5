from django.shortcuts import render,redirect
from .forms import MentorRegisterForm
from .forms import MenteeRegisterForm

# Create your views here.


def about(request) :
    return render(request,"about.html")

def register_mentor(request):
    if request.method=="POST":
        form=MentorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=MentorRegisterForm()    
    return render(request,"rough.html",{"form":form})

def register_mentee(request):
    if request.method=="POST":
        form=MenteeRegisterForm(request.POST)
        Male=MenteeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about/')
    else:
        form=MenteeRegisterForm()    
    return render(request,"rough.html",{"form":form})
