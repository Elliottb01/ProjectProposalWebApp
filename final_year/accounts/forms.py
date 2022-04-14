import email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class CreateProfile(forms.ModelForm):
    class Meta:
        model = models.Lecture
        fields=['title','first_name','last_name', 'email', 'number', 'faculty']
