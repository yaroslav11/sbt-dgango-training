from django.contrib import admin


from .models import *

#class AutoQuestion():


admin.site.register(Question, admin.ModelAdmin)