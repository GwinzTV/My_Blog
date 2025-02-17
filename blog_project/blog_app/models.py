# blog_app/models.py

from django.db import models

# Create your models here.


class BlogPost(models.Model):   # Table name will be blog_app_blogpost
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)

    def __str__(self):  # This allows the blogpost to be identified by title in the admin panel
        return self.title
