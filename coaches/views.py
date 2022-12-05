from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CoachForm
from .models import Coach


#List of all coaches
coaches_list = Coach.objects.all()

def coaches(request):
    coach_obj = Coach.objects.all()
    context = {'coaches' : coach_obj}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    for coach in coaches_list:
        if pk == coach.name:
            coachObj = Coach.objects.get(name=pk)
            context = {'coach':coachObj}
            return render(request,'coach.html',context)
    return HttpResponse(f"Could not find {pk} coach page")

@login_required(login_url="login")
def addCoach(request):
    form = CoachForm()

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(f"{type(form['name'])}Coach Added")
            return redirect('coaches')

    context = {'form' : form}
    return render(request, 'coach_form.html', context)

@login_required(login_url="login")
def updateCoach(request, pk):
    coach = Coach.objects.get(name=pk)
    form = CoachForm(instance=coach)
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('coaches')

    context = {'form' : form, 'coach' : coach}
    return render(request, 'coach_form.html', context)

@login_required(login_url="login")
def deleteCoach(request, pk):
    coach = Coach.objects.get(name=pk)

    if request.method == 'POST':
        coach.delete()
        return redirect('coaches')
    context = {'coach' : coach}
    return render(request,'delete_template.html', context)