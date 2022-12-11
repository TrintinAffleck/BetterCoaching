from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def UserUpdated(sender, instance, created, **kwargs):
    if created == False:
        print("User Updated")
        print(f"Username: {instance}")
        return
    print("User Added")
    print(f"Username: {instance}")

@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created == True:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
            is_coach = False,
        )

'''Updates the user information if the profile is changed.'''
@receiver(post_save,sender=Profile)
def UpdateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        if profile.username != None:
            user.username = profile.username
        else:
            user.username = profile.user
        user.email = profile.email
        user.save()

@receiver(post_delete,sender=Profile)
def DeleteUser(sender, instance, **kwargs):
    profile = instance
    user = profile
    user.delete()
