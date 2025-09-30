from django.shortcuts import render
from .models import Student

# Create your views here.

def helo(request):
    return render(request,'index.html')


def dashboard_view(request):
    info=Student.objects.filter(user=request.user)
    return render(request,'dashboard.html',{'info':info})
