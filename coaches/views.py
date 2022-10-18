from django.shortcuts import render
from django.http import HttpResponse
from .models import Coach
def coaches(request):
    coach_obj = Coach.objects.all()
    context = {'coaches' : coach_obj}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    coachObj = Coach.objects.get(id=pk)
    return render(request,'coach.html',{'coach' : coachObj})