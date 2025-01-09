from django.contrib.auth.decorators import login_required
from django.contrib.messages import success, error
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from .models import Profile
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from coaches.utils import paginate_coaches, search_coaches

from .forms import AccomplishmentForm, AddCoachForm, CoachForm, ReviewForm
from .models import Coach


def coaches(request: WSGIRequest):
    coach_obj, search_query = search_coaches(request)
    custom_range,coaches = paginate_coaches(request, coach_obj, 3)
    for coach in coach_obj:
        if coach.rating_total <= 1:
            coach.rating_ratio = coach.rating_total
    context = {'coaches' : coaches, 'search_query': search_query,
               'custom_range' : custom_range}
    return render(request,'coaches_list.html', context)

def coach(request: WSGIRequest,pk):
    for coach in Coach.objects.all():
        if pk.lower() == coach.display_name.lower():
            if request.method == 'POST':
                form = ReviewForm(request.POST)
                if form.is_valid():
                    review = form.save(commit=False)
                    review.coach = coach
                    review.owner = request.user.profile
                    review.save()
                    form = ReviewForm()
                    success(request,'Submitted review')
                else:
                    error(request, 'Form was invalid.')
            else:
                form = ReviewForm()
            coach.get_average
            coach.save()
            context = {'coach' : coach, 'forms': form}
            return render(request, 'coach.html', context)
    return HttpResponse(f"Could not find coach with name {pk}")

@login_required(login_url='login')
@permission_classes([IsAdminUser])
def addCoach(request: WSGIRequest):
    form = AddCoachForm()
    if request.method == 'POST':
        form = AddCoachForm(request.POST)
        if form.is_valid():
            coach = form.save(commit=False)
            coach, created = Coach.objects.get_or_create(
                user=coach.user,
                display_name=coach.display_name,
                headline=coach.headline,
                body=coach.body,
                rating_total=0,
                rating_ratio=0,
            )
            user = User.objects.get(username=coach.user)
            if user:
                user.profile.is_coach = True
                user.save()
                profile = Profile.objects.get(user=user)
                profile.save()
            if created:
                success(
                    request, f'Coach {coach.display_name} Successfully Added')
                coach.save()
            else:
                error(request, f'{coach.display_name} Coach Already Exists.')
                
            return redirect('coaches')

    context = {'form': form}
    return render(request, 'add-coach-form.html', context)

@login_required(login_url='login')
def updateCoach(request: WSGIRequest):
    if not request.user.profile.is_coach:
      return HttpResponse("You are not a coach!")
    profile = request.user.profile
    
    coach = Coach.objects.get(user=profile)
    form = CoachForm(instance=coach)
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('coaches')

    context = {'form' : form, 'coach' : coach}
    return render(request, 'coach_dashboard.html', context)

@login_required(login_url='login')
@permission_classes([IsAdminUser])
def deleteCoach(request: WSGIRequest, pk):
    coach = Coach.objects.get(name=pk)
    if request.method == 'POST':
        coach.delete()
        return redirect('coaches')
    context = {'coach' : coach}
    return render(request,'delete_template.html', context)

@login_required(login_url='login')
def addAccomplishment(request: WSGIRequest):
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