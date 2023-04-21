from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.messages import success
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from .forms import CoachForm, AccomplishmentForm, ReviewForm
from .models import Coach
from coaches.utils import search_coaches, paginate_coaches

coaches_list = Coach.objects.all()

def coaches(request):
    coach_obj, search_query = search_coaches(request)
    custom_range,coaches = paginate_coaches(request, coach_obj, 3)

    context = {'coaches' : coaches, 'search_query': search_query,
               'custom_range' : custom_range}
    return render(request,'coaches_list.html', context)

def coach(request,pk):
    for coach in coaches_list:
        if pk.lower() == coach.display_name.lower():
            coachObj = Coach.objects.get(display_name=pk)
            form = ReviewForm()
            if request.method == 'POST':
                form = ReviewForm(request.POST)
                review = form.save(commit=False)
                review.coach = coachObj
                review.owner = request.user.profile
                review.save()
                coachObj.get_votes
                success(request,'Submitted review')
            context = {'coach' : coachObj, 'form' : form}
            return render(request,'coach.html',context)

    return HttpResponse(f'Could not find {pk} coach page.')

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
def updateCoach(request):
    profile = request.user.profile
    coach = Coach.objects.get(user_type=profile)
    form = CoachForm(instance=coach)
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coaches')

    context = {'form' : form, 'coach' : coach}
    return render(request, 'coach_form.html', context)

@login_required(login_url='login')
@permission_classes([IsAdminUser])
def deleteCoach(request, pk):
    coach = Coach.objects.get(name=pk)
    if request.method == 'POST':
        coach.delete()
        return redirect('coaches')
    context = {'coach' : coach}
    return render(request,'delete_template.html', context)

@login_required(login_url='login')
def addAccomplishment(request):
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