from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import Profile
from .ranks import RANKS, DIVISIONS

'''Creates a profile for the user'''
@receiver(post_save, sender=User, dispatch_uid="create_profile")
def CreateProfile(sender, instance, created, **kwargs):
    if created == True:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            # Need to use list comprehension because RANKS & DIVISIONS are tuple of tuples
            rank=[i[1] for i in RANKS if i[1] == 'UNRANKED'][0],
            division=[i[1] for i in DIVISIONS if i[1] == ''][0],
            name=user.first_name,
            is_coach=False,
        )
        send_mail(
            'Welcome to better coaching!',
            'Thank you for joining better coaching.',
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

'''Updates the user information if the profile is changed.'''
@receiver(post_save, sender=Profile, dispatch_uid="update_user")
def UpdateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.rank = profile.rank
        user.division = profile.division
        user.save()
        
'''Handles Deletion of user if the profile is deleted'''
@receiver(pre_delete, sender=Profile, dispatch_uid="delete_user")
def DeleteUser(instance, **kwargs):
        user = instance.user
        user.delete()