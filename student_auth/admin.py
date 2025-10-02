from django.contrib import admin

# Register your models here.

from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display=('student','nickname','bio')
    list_filter=('student__Rollno',)
    ordering=('student__Rollno',)




admin.site.register(Profile,ProfileAdmin)