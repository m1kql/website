from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# Add Posts model
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='Uncategorized', choices= Category.objects.all().values_list('name','name'))
    snippet = models.CharField(max_length=255, default='Click to read more...' )
    body = RichTextUploadingField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
