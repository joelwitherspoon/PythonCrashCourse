from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
        """A blogpost entry in the blog"""
        title = models.CharField(max_length=200)
        text = models.TextField()
        date_added = models.DateTimeField(auto_now_add=True)
        owner = models.ForeignKey(User,on_delete=models.CASCADE)
        is_public = models.BooleanField(default=False)
        
        class Meta:
            verbose_name_plural = 'blogposts'
        
        def __str__(self):
            """Return a string representation of the model"""
            if len(self.title) < 50:
                return self.title
            else:
                return self.title[:50] + "..."
        