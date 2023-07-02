from django.db import models

# Create your models here.

CHOICES = [
        ("1", "3-6"),
        ("2", "6-9"),
        ("3", "12-3"),
        ("4", "9-12"),
       
    ]

AGE_CHOICES=[
        ("1", "14-17"),
        ("2", "18-24"),
        ("3", "25-34"),
        ("4", "35-44"),
] 

EDUCATION_CHOICES=[
        ("1", "Graduation"),
        ("2", "Pursuing Graduation"),
        ("3", "Diploma"),
        ("4", "Pursuing Diploma"),
        ("5", "Others"),
]  

class CustomMentor(models.Model):

    Name=models.CharField(max_length=400,default="")
    Email=models.EmailField(default="")
    Password=models.CharField(max_length=400,default="")
    Qualification=models.CharField(max_length=200,default="")
    English=models.BooleanField()
    Hindi=models.BooleanField()
    Kannada=models.BooleanField()
    Monday=models.CharField(max_length=300, choices = CHOICES)
    Tuesday=models.CharField(max_length=300, choices = CHOICES)
    Wednesday=models.CharField(max_length=300, choices = CHOICES)
    Thursday=models.CharField(max_length=300, choices = CHOICES)
    Friday=models.CharField(max_length=300, choices = CHOICES)
    Saturday=models.CharField(max_length=300, choices = CHOICES)
    Sunday=models.CharField(max_length=300, choices = CHOICES)


    def __str__(self):
        return self.Name


class CustomMentee(models.Model):

    Name=models.CharField(max_length=400,default="")
    Email=models.EmailField()
    Password=models.CharField(max_length=400,default="")
    Phone=models.CharField(max_length=10,default="")
    Male=models.BooleanField() ##we have reject males 
    Female=models.BooleanField()
    DOB=models.DateField(default="xx/xx/xxxx")
    Age=models.CharField(max_length=300, choices = AGE_CHOICES)
    English=models.BooleanField()
    Hindi=models.BooleanField()
    Kannada=models.BooleanField()
    Current_Address=models.CharField(max_length=400)
    Permanent_Address=models.CharField(max_length=400)
    Education_status=models.CharField(max_length=300, choices = EDUCATION_CHOICES)


    def __str__(self):
        return self.Name        