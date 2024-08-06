from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    Firstname = forms.CharField(max_length=60,label='Firstname',required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Your first name',
                                                             'class': 'form-control',
                                                             }))
    Lastname = forms.CharField(max_length=60,label='Lastname',required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Your Lastname',
                                                             'class': 'form-control',
                                                             }))
    email =forms.EmailField(required=True,label='email',
                                 widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(max_length=65,label='Password',required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter Your Password',
                                                             'class': 'form-control',
                                                             }))
    password2 = forms.CharField(max_length=65,label='Confirm Password',required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Retype Password',
                                                             'class': 'form-control',
                                                             }))
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control'
                                                             }))
    
    
     
