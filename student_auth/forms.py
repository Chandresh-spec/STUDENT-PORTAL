from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    
    class Meta:
        email=forms.EmailField(required=True)
        model=User
        fields=('username','email','password1','password2')

        def clean_username(self):
            username=self.cleaned_data.get("username")
            return username.lower()
        

        def clean_email(self):
            email=self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("this email is already registered.")
            return email
