from multiprocessing import context
from pyexpat import model
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.forms import forms
from django.urls import reverse_lazy
from . import forms
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .models import Lecture
from .forms import CreateProfile, user_login_form, user_sighup_Form
from django.views import generic

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = user_sighup_Form(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            
            return redirect('projects:list')
    else:
        form = user_sighup_Form()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = user_login_form(data=request.POST)
        if form.is_valid():
            #log in user
            user= form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('projects:list')

    else:
        form = user_login_form()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('projects:list')

class show_profile_page(DetailView):
    model = Lecture
    template_name = 'accounts/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Lecture.objects.all()
        context = super(show_profile_page, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Lecture, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class edit_profile_page(generic.UpdateView):
    model = Lecture
    template_name = 'accounts/profile_edit.html'
    fields = ['profilepic', 'title', 'first_name', 'last_name', 'office', 'email', 'number', 'faculty', 'lec_description']
    success_url = reverse_lazy ('homepage')





