from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message
from coaches.models import Coach
from .forms import CustomUserCreationForm, UpdateAccountForm, MessageForm


def loginUser(request):
    page = 'login'
    context = {'page': page}

    if request.user.is_authenticated:
        return redirect('coaches')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            try:
                user = authenticate(
                    request, username=username, password=password)
                login(request, user=user)
                return redirect(request.GET['next'] if 'next' in request.GET else 'coaches')
            except:
                messages.error(request, 'Password is incorrect.')
                return render(request, 'users/login_registration.html', context)

        except:
            messages.error(request, 'Username does not exist')
            return render(request, 'users/login_registration.html', context)

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
            messages.error(
                request, 'Username is taken. Please try another username.')
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


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    user_messages = profile.messages.all()
    unread_count = user_messages.filter(is_read=False).count()
    context = {'unread_count': unread_count,
               'user_messages': user_messages}
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    print(f"{message.is_read} triggered")
    context = {'profile':profile,'message':message}
    return render(request, 'users/message.html', context)

@login_required(login_url='login')
def sendMessage(request,pk):
    coach = Coach.objects.get(id=pk)
    receiver = coach.user_type
    form = MessageForm()
    context = {'form':form}
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.profile
            message.receiver = receiver
            message.save()
            messages.success(request, 'Message Sent')
    return render(request,'message_form.html', context)