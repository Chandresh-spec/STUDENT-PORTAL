from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from .models import Profile



# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        

        return render(request,'signup.html',{'form':form})
    
    else:
        form=SignupForm()
    
    return render(request,'signup.html',{'form':form})



def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():

            user=form.get_user()
           
            login(request,user)
            return redirect('home')
            
    else:
            form=AuthenticationForm()
        
    return render(request,'login.html',{'form':form})
            


def logout_view(request):
     
     logout(request)
     return redirect('home')




def profile_view(request):
     profile=Profile.objects.get(student__user=request.user)
     return render(request,'profile.html',{'profile':profile})
    