from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UpdateAccountForm

def loginUser(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('coaches')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'coaches')
        else:
            messages.error(request, 'Username or Password is incorrect.')
    return render(request, 'users/login_registration.html', context)


def registerUser(request):
    page = 'register'
    forms = CustomUserCreationForm()
    if request.method == 'POST':
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            user = forms.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account Successfully created.')
            login(request, user)
            return redirect('coaches')
        else:
            if request.POST['password1'] != request.POST['password2']:
                messages.error(request, 'Passwords must match')
                return redirect('register')
            messages.error(request, 'Username is taken. Please try another username.')
            return redirect('register')

    context = {'page': page, 'forms': forms}
    return render(request, 'users/login_registration.html', context)


def logoutUser(request):
    messages.success(request, 'Logged out.')
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editUserAccount(request):
    profile = request.user.profile

    form = UpdateAccountForm(instance=profile)
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Information Updated.')
    context = {'form': form}
    return render(request, 'users/account.html', context)
