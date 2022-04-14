from dataclasses import field
from tkinter import Widget
import django
from django import forms
from . import models

#form for project creation, fields indicate the fields which will be displayed to fill out by user

class CreateProject(forms.ModelForm):
    class Meta:
        model = models.Project
        fields=['title','description', 'conceptual', 'programming', 'technical', 'status', 'Skill','subject']
        exclude = ['lecture']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'conceptual': forms.Select(attrs={'class': 'form-control'}),
            'programming': forms.Select(attrs={'class': 'form-control'}),
            'technical': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'Skill': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'subject': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }