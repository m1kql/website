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
from .models import Post

#home view
def home(request):
    return render(request, 'home.html', {})

#about me page
def AboutView(request):
    return render(request, 'about.html')

#view my projects
def ProjectsView(request):
    return render(request, 'projects.html')

#view my timeline
def TimelineView(request):
    return render(request, 'timeline.html')

#view contact form + contact form submission
def SocialView(request):
    if request.method == 'POST':
        message = request.POST['message']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        template = get_template('contact_template.txt')
        context = {
            'contact_fname': firstname,
            'contact_lname': lastname,
            'contact_email': email,
            'form_content': message,
        }

        content = template.render(context)

        send_mail(
            'New contact form submission:', 
            content, 
            settings.EMAIL_HOST_USER,
            ['liang.mike.to@gmail.com'],
            fail_silently=False
            )
    return render(request, 'contact.html')


#View categories
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

#view blog posts 
class PostView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']

#view artcle details (blog posts)
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'