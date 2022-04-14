from ast import Del
from cProfile import Profile
from contextvars import Context
from dataclasses import fields
import imp
from multiprocessing import context
from pyexpat import model
import re
from this import d
from turtle import title
from urllib import request
from webbrowser import get
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import Project, Skill
from django.contrib.auth.decorators import login_required
from .forms import CreateProject
from .filters import project_filter
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views import generic 
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from accounts.models import Lecture
from django.contrib.auth.models import User



# Create your views here.
#def project_list(request):
#    projects = Project.objects.all().order_by('title')
#    return render(request, 'projects/project_list.html', {'projects': projects})

class project_list(ListView):
    model = Project
    template_name = 'projects/project_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = project_filter(self.request.GET, queryset=self.get_queryset())
        return context   

class show_project_details(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, *args, **kwargs):
        proj_detail = Project.objects.all()
        context = super(show_project_details, self).get_context_data(*args, **kwargs)
        proj_detail = get_object_or_404(Project, id=self.kwargs['pk'])
        context["proj_detail"] = proj_detail

        stuff = get_object_or_404(Project, id=self.kwargs['pk'])
        p_skill = stuff.p_skill()
        context["p_skill"] = p_skill

        #gathers all information relating to the current selected project does this by using the project id
        stuff2 = get_object_or_404(Project, id=self.kwargs['pk'])
        p_subject = stuff2.p_subject() #passess information only relating to the subject field into p_subject
        context["p_subject"] = p_subject #set variable equal to results for subjects
        return context

    
#view model ensure that users a logged in before been able to create post, if user is not then redirects to login page
#@login_required(login_url="/accounts/login/" )
#when post method is called will execude the below code, makes sure form is valid then saves to database
#def project_create(request):
 #   if request.method == 'POST':
 #       form = forms.CreateProject(request.POST, request.FILES)
 #       if form.is_valid():
            #save to databse
  #          instance = form.save(commit=False)

 #           instance.save()
  #          form.save_m2m()
  #          return redirect('projects:list')
#if not valid redirects them back to form saying whats wrong
 #   else: 
 #       form=forms.CreateProject()
 #   return render(request, 'projects/project_create.html', {'form': form})

class update_project(UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    fields = ['title','description', 'conceptual', 'programming', 'technical', 'status', 'Skill','subject']


class project_create(CreateView):
    model = Project
    template_name = 'projects/project_create.html'
    form_class = CreateProject

    #when a new project is created the lecture field is automatically set to the currently logged in user
    def form_valid(self, form):
        instance = form.save(commit=False)
        puser = get_object_or_404(Lecture, id=self.request.user.pk)
        luser =get_object_or_404(User, id=self.request.user.pk)
        instance.lecture = puser
        instance.lecture2 = luser
        instance.save()
        return redirect('projects:list')





class project_delete(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('projects:list')
