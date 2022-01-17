''' This file is created to automatically create profile for new users '''
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

''' Here User is going to be the sender who will send signal '''
''' Reciever is going to be a function which will recieve this signal and performs a task '''


# It is recieving a signal that a user is saved(created)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # if user is created
    if created:
        # create a profile
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()