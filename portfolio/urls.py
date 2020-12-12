from django.urls import path
from . import views
from .views import home, AboutView, ProjectsView, SocialView

urlpatterns = [
    path('', views.home, name= "home"),
    path('aboutme/', views.AboutView, name="about"),
    path('myprojects/', views.ProjectsView, name="projects"),
    path('socials/', views.SocialView, name= "social"),
]