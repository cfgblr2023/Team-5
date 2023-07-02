from django import forms
from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import CustomMentor
from .models import CustomMentee

# Create your forms here.



class MentorRegisterForm(forms.ModelForm):
    Name=forms.CharField(required=True)
    Email=forms.EmailField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput)
    Qualification=forms.CharField(max_length=200,required=True)
    English=forms.BooleanField(required=False)
    Hindi=forms.BooleanField(required=False)
    Kannada=forms.BooleanField(required=False)


    class Meta:
        model = CustomMentor
        fields = ("Name","Email","Password","Qualification","English","Hindi","Kannada","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
                
    
    def clean_Password(self):
        password = self.cleaned_data.get('Password')
        num_count = sum(char.isdigit() for char in password)

        if len(password) < 4 or num_count < 2:
            raise ValidationError("Password must have at least 4 characters and 2 numbers.")

        return password

    def clean_Name(self):
        Name = self.cleaned_data.get('Name')
        if CustomMentor.objects.filter(Name=Name).exists():
            raise forms.ValidationError('This Name is already taken.')
        return Name 

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.initial = ''       


class MenteeRegisterForm(forms.ModelForm):
    Name=forms.CharField(required=True)
    Email=forms.EmailField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput)
    Qualification=forms.CharField(max_length=200,required=True)
    English=forms.BooleanField(required=False)
    Hindi=forms.BooleanField(required=False)
    Kannada=forms.BooleanField(required=False)
   


    class Meta:
        model = CustomMentee
        fields = ("Name","Email","Password","Phone","Male","Female","DOB","Age","English","Hindi","Kannada","Current_Address","Permanent_Address","Education_status")
                
   
    def clean_Password(self):
        password = self.cleaned_data.get('Password')
        num_count = sum(char.isdigit() for char in password)

        if len(password) < 4 or num_count < 2:
            raise ValidationError("Password must have at least 4 characters and 2 numbers.")

        return password

    def clean_Name(self):
        Name = self.cleaned_data.get('Name')
        if CustomMentee.objects.filter(Name=Name).exists():
            raise forms.ValidationError('This Name is already taken.')
        return Name  

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.initial = ''           