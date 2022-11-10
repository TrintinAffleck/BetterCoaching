from django.shortcuts import render

def profiles(request):
    return render(request,'users/profile.html')
