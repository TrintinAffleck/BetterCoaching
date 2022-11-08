from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CoachForm
from .models import Coach

#List of all coaches
coaches_list = Coach.objects.all()

def coaches(request):
    coach_obj = Coach.objects.all()
    context = {'coaches' : coach_obj}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    for ch in coaches_list:
        if pk == ch.name:
            coachObj = Coach.objects.get(name=pk)
            return render(request,'coach.html',{'coach' : coachObj})
    return HttpResponse(f"Could not find {pk} coach page")

def addCoach(request):
    form = CoachForm()

    if request.method == 'POST':
        print(request.POST)
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Coach Added")
            return redirect('coaches')
        else:
            print("form is invalid")

    context = {'form' : form}
    return render(request, 'coach_form.html', context)

def updateCoach(request, pk):
    coach = Coach.objects.get(id=pk)
    form = CoachForm(instance=coach)

    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coaches')

    context = {'form' : form, 'coach' : coach}
    return render(request, 'coach_form.html', context)

def deleteCoach(request, pk):
    coach = Coach.objects.get(id=pk)

    if request.method == 'POST':
        coach.delete()
        return redirect('coaches')
    context = {'coach' : coach}
    return render(request,'delete_template.html', context)