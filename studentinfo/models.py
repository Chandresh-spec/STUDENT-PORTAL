from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    cls_choice=[
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('BCOM','BCOM'),
        ('MCA','MCA'),
    ]
    year_choice=[
        ('1YEAR','1YEAR'),
        ('2YEAR','2YEAR'),
        ('3YEAR','YEAR'),
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    Rollno=models.CharField(max_length=10)
    cls=models.CharField(max_length=5,choices=cls_choice,null=False,blank=False)
    current_year=models.CharField(max_length=5,choices=year_choice,blank=False,null=True)
    email=models.EmailField(default='chandu@gmail.com',null=False)


    def __str__(self):
        return f"{self.name},{self.Rollno}"
    



