from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#home view
def home(request):
    return render(request, 'home.html', {})

#about me page
def AboutView(request):
    return render(request, 'about.html')

#view my projects
def ProjectsView(request):
    return render(request, 'projects.html')
