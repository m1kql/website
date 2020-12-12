from django.urls import path
from . import views
from .views import home, AboutView, ProjectsView, SocialView, PostView, ArticleDetailView, CategoryView, AddPostView, UpdatePostView, UpdateView, DeletePostView

urlpatterns = [
    path('', views.home, name= "home"),
    path('aboutme/', views.AboutView, name="about"),
    path('myprojects/', views.ProjectsView, name="projects"),
    path('socials/', views.SocialView, name= "social"),
    path('timeline/', views.TimelineView, name="timeline"),
    path('blog/', PostView.as_view(), name="blog"),
    path('category/<str:cats>/', CategoryView, name= 'category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),

    path('addpost/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/removepost', DeletePostView.as_view(), name="delete_post"),
    path('article/editlist/', UpdateView.as_view(), name="updatelist"),
]