from django.contrib import admin

# Register your models here.

from App.models import CustomMentor
from App.models import CustomMentee
# Register your models here.
admin.site.register(CustomMentor)
admin.site.register(CustomMentee)
