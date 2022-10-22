from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoachForm
from .models import Coach


def coaches(request):
    coach_obj = Coach.objects.all()
    context = {'coaches' : coach_obj}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    coachObj = Coach.objects.get(id=pk)
    return render(request,'coach.html',{'coach' : coachObj})

def addCoach(request):
    form = CoachForm()

    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coaches')

    context = {'form' : form}
    return render(request, 'coach_form.html', context)

def updateCoach(request, pk):
    coach = Coach.objects.get(id=pk)
    form = CoachForm(instance=coaches)

    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coaches)
        if form.is_valid():
            form.save()
            return redirect('coaches')

    context = {'form' : form}
    return render(request, 'coach_form.html', context)