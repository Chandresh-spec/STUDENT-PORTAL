from django.shortcuts import render,redirect
from .forms import SignupForm

# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request,'signup.html',{'form':form})
    

    else:
        form=SignupForm()
        return render(request,'signup.html',{'form':form})