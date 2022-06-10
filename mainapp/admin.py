from django.contrib import admin
from .models import *

class adminModel(admin.ModelAdmin):
    list_display=["__str__",'pk', 'items']

admin.site.register(plan,adminModel) 