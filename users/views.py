from django.shortcuts import render
from .models import Profile
from coaches.models import Coach

def profiles(request):
    profiles = Profile.objects.all
    coaches = Coach.objects.all
    context = {'coaches' : coaches, 'profiles' : profiles}
    return render(request,'users/profile.html',context)
