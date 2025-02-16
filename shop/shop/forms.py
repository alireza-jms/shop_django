from django.contrib.auth.models import User #برای ثبت نام 
from django.contrib.auth.forms import UserCreationForm #برای ثبت نام 
from django import forms
from django.template import loader

class signupforms(UserCreationForm):
  first_name = forms.CharField(
    label="",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خود را وارد کنید'})
  )
  last_name = forms.CharField(
    label="",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام خانوادگی را وارد کنید'})
  )
  email = forms.EmailField(
    label="",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ایمیل خود راوارد کنید'})
  )
  username = forms.CharField(
    label="",
    max_length=50,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'نام کاربری '})

  )
  password1= forms.CharField(
    label='',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'name':'password',
        'type':'password',
        'placeholder':'رمز بالا 8 کاراکتر را وارد کنید'
      }
    )
  )
  password2= forms.CharField(
    label='',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'name':'password',
        'type':'password',
        'placeholder':'رمز خود را دوباره وارد کنید'
      }
    )
  )
  class Meta:
    model=User
    fields=('first_name', 'last_name', 'email', 'username','password1','password2')