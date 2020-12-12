from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('aboutme/', views.AboutView, name="about"),
    path('myprojects/', views.ProjectsView, name="projects"),
]