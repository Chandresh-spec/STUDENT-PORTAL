from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    Rollno=models.CharField(max_length=10)
    email=models.EmailField(null=False)


    def __str__(self):
        return f"{self.name},{self.Rollno}"



class Assignment(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    assignment1=models.BooleanField(default=False)
    assignment2=models.BooleanField(default=False)
    due_date1=models.DateField(default=timezone.now)
    due_date2=models.DateField(default=timezone.now)
    img1=models.ImageField(upload_to='ass1/',null=True,blank=True)
    img2=models.ImageField(upload_to='ass2/',null=True,blank=True)


    def __str__(self):
        return f"Assignmnets for {self.student.name}"



class Course(models.Model):
    course_choice=[
        ('BCA','BCA'),
        ('BCOM','BCOM'),
        ('BBA','BBA'),

    ]
    year_choice=[
        (1,'1st Year'),
        (2,'2nd Year'),
        (3,'3rd Year'),
        ]

    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=10,choices=course_choice)
    current_year=models.IntegerField(max_length=10,choices=year_choice)

    def __str__(self):
        return f"{self.course_name} - {self.student.name}"
    


class Marks(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    Course_name=models.OneToOneField(Course,on_delete=models.CASCADE)
    marks=models.FloatField(default=0)


    












