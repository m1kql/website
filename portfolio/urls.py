from django.urls import path
from . import views
from .views import home, AboutView, ProjectsView, SocialView, PostView, CategoryView, ArticleDetailView

urlpatterns = [
    path('', views.home, name= "home"),
    path('aboutme/', views.AboutView, name="about"),
    path('myprojects/', views.ProjectsView, name="projects"),
    path('socials/', views.SocialView, name= "social"),
    path('timeline/', views.TimelineView, name="timeline"),
    path('blog/', PostView.as_view(), name="blog"),
    path('category/<str:cats>/', CategoryView, name= 'category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
]