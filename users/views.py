from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from coaches.models import Coach
from .forms import CustomUserCreationForm, UpdateAccountForm, UpdateCoachForm


def profiles(request):
    profiles = Profile.objects.all
    coaches = Coach.objects.all
    context = {"coaches": coaches, "profiles": profiles}
    return render(request, "users/profile.html", context)


def loginUser(request):
    page = "login"
    context = {"page": page}

    if request.user.is_authenticated:
        return redirect("coaches")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(request.POST)

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect("coaches")
        else:
            messages.error(request, "Username or Password is incorrect.")
    return render(request, "users/login_registration.html", context)


def registerUser(request):
    page = "register"
    forms = CustomUserCreationForm()
    if request.method == "POST":
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Account Successfully created.")
            login(request, user)
            return redirect("coaches")
        else:
            if request.POST["password1"] != request.POST["password2"]:
                messages.error(request, "Passwords must match")
                return redirect("register")
            messages.error(request, "Username is taken. Please try another username.")
            return redirect("register")

    context = {"page": page, "forms": forms}
    return render(request, "users/login_registration.html", context)


def logoutUser(request):
    messages.success(request, "Logged out.")
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def editUserAccount(request):
    profile = request.user.profile
    form = UpdateAccountForm()
    if request.method == "POST":
        form = UpdateAccountForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "users/account.html", context)

@login_required(login_url="coaches")
def editCoachAccount(request):
    profile = request.user.profile
    form = UpdateCoachForm()
    if profile.is_coach and request.method == "POST":
        form = UpdateCoachForm(request.POST, request.FILES, empty_permitted=False)
        if form.is_valid():
            form.save()
            #create coach
            context = {"form" : form}
            messages.success(request,"Updated your coach page.")
            return render(request, 'coach_dashboard.html', context)
    else:
        return redirect('coaches')
