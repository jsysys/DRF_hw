from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(default = timezone.now())
    complete = models.BooleanField(default = True)
    important = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
