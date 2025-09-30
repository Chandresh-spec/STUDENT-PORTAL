from django.contrib import admin
from .models import Student,Assignment

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','Rollno','current_year')
    ordering=('Rollno',)
    search_fields=('Rollno','name')
    list_filter=('cls','Rollno')




admin.site.register(Student,StudentAdmin)



class AssAdmin(admin.ModelAdmin):
    list_display=('student','assignment1','assignment2','due_date1','due_date2')
    ordering=('student__Rollno',)
    search_fields=('student__Rollno','student__name')
    list_filter=('assignment1','assignment2')


admin.site.register(Assignment,AssAdmin)



class StudentCourse(admin.ModelAdmin):
    list_display=('student','course_name','current_year')
    ordering=('student__Rollno',)
    list_filter=('current_year','course_name')


    