from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Each class is converted to database by Django
class Post(models.Model):
    # Each attribute is field in database
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if author is deleted, delete the post as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # to print details of user using print in a customized way
    def __str__(self):
        return self.title
    
    # to define, where to go when post is created
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
