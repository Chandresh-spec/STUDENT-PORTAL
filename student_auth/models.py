from django.db import models
from studentinfo.models import Student

# Create your models here.

class Profile(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=100,null=False)
    email=models.EmailField(null=False)
    photo=models.ImageField(upload_to='profile_photo/',null=True,blank=True)
    bio=models.TextField(max_length=200)

    def __str__(self):
        return f"{self.student}--{self.nickname}"