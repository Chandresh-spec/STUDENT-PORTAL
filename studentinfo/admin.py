from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','Rollno','cls','current_year')
    ordering=('Rollno',)
    search_fields=('Rollno','name')
    list_filter=('cls','Rollno')




admin.site.register(Student,StudentAdmin)