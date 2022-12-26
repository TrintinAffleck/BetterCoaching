from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from .ranks import RANKS, DIVISIONS
    
'''Creates a profile for the user'''
@receiver(post_save, sender=User)
def CreateProfile(sender, instance, created, **kwargs):
    if created == True:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            rank=[i[1] for i in RANKS if i[1] == 'UNRANKED'][0], #Need to use list comprehension because RANKS & DIVISIONS are tuple of tuples
            division= [i[1] for i in DIVISIONS if i[1] == ''][0],
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
        user.username = profile.username
        user.email = profile.email
        user.rank = profile.rank
        user.division = profile.division
        user.save()

@receiver(post_delete,sender=Profile)
def DeleteUser(sender, instance, **kwargs):
    profile = instance.user
    print(f'Profile: {profile}')
    user = profile
    user.delete()
