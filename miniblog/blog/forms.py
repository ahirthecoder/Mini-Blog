from .models import post
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email']
        labels ={'first_name': 'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control my-2'}),
        'first_name':forms.TextInput(attrs={'class':'form-control my-2'}),
        'last_name':forms.TextInput(attrs={'class':'form-control my-2'}),
        'email':forms.EmailInput(attrs={'class':'form-control my-2'})
         }

class LoginForm(AuthenticationForm):
    username =UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password =  forms.CharField(label=("Password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplte': 'current-password','class':'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields =['title','desc']
        labels = {'title':'Title', 'desc': 'Description'}
        widget = {
            'title':forms.TextInput(attrs=
            {'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }

