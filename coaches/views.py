from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.messages import success,warning,info
from .forms import CoachForm, AccomplishmentForm
from .models import Coach
from coaches.utils import search_coaches, paginate_coaches

#List of all coaches
coaches_list = Coach.objects.all()

def coaches(request):
    coach_obj, search_query = search_coaches(request)
    custom_range,coaches = paginate_coaches(request, coach_obj, 1)

    context = {'coaches' : coaches, 'search_query': search_query,
               'custom_range' : custom_range}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    for coach in coaches_list:
        if pk == coach.display_name:
            coachObj = Coach.objects.get(display_name=pk)
            context = {'coach':coachObj}
            return render(request,'coach.html',context)
    return HttpResponse(f'Could not find {pk} coach page')

@login_required(login_url='login')
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

@login_required(login_url='login')
def updateCoach(request, pk):
    coach = Coach.objects.get(name=pk)
    form = CoachForm(instance=coach)
    profile = request.user
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            coach_obj = form.save(commit=False)
            if coach:
                print(f'Coach : {coach}')
                print(f'Profile : {profile}')
                if coach.user_type == profile:
                    coach_obj.user_type = profile
            form.save()
            return redirect('coaches')

    context = {'form' : form, 'coach' : coach}
    return render(request, 'coach_form.html', context)

@login_required(login_url='login')
def deleteCoach(request, pk):
    coach = Coach.objects.get(name=pk)

    if request.method == 'POST':
        coach.delete()
        return redirect('coaches')
    context = {'coach' : coach}
    return render(request,'delete_template.html', context)


def addAccomplishment(request,pk):
    profile = request.user.profile
    form = AccomplishmentForm()
    if request.method == 'POST':
        form = AccomplishmentForm(request.user)
        if profile.is_coach:
            if form.is_valid():
                skill = form.save(commit=False)
                skill.owner = profile
                skill.save()
                success(request, "Accomplishment Added")
                return redirect('add-accomplishment')

    context = {'profile' : profile, 'form' : form}
    return render(request, 'accomplishment_form.html', context)