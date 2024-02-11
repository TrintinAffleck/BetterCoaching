from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from .models import Profile
from coaches.models import Coach
from .ranks import DIVISIONS, RANKS

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
        if profile.is_coach:
            try:
                coach_obj, is_coach = Coach.objects.get_or_create(
                        user = profile,
                        display_name = profile.username,
                        headline = "",
                        body = "",
                        discord_link = ""
                )
                if is_coach:
                    coach_obj.save()
            except Exception as e:
                print(e)
                print(f"Exception was thrown in the {function.__name__}")
        else:
            Coach.objects.filter(user=profile).delete()
        user.save()
        
'''Handles Deletion of user if the profile is deleted'''
@receiver(post_delete, sender=Profile, dispatch_uid="delete_user")
def DeleteUser(instance, **kwargs):
        try:
            user = instance.user
            user.profile.delete()
            user.delete()
        except RecursionError as e:
            print("Recursion Error in DeleteUser signal.")
            print(e.message)