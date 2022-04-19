from dataclasses import fields
import email
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . import models
from tkinter import Widget


class CreateProfile(forms.ModelForm):
    class Meta:
        model = models.Lecture
        fields=['title','first_name','last_name', 'email', 'number', 'faculty']

class user_sighup_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2',]

        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 50%;'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        help_texts={
            'username':None,
            'password1':None,
            'password2':None,
            'password':None,
        }

class user_login_form(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }