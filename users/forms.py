from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'email', 'username', 'password1', 'password2',
        ]
        labels = {'first_name': 'Name'}

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name != 'password2':
                field.widget.attrs.update({'class': 'input','class': 'form-control', 'class': 'mb-3'})
            if name == 'first_name':
                field.widget.attrs.update({'placeholder': 'Enter First Name.'})
            if name == 'email':
                field.widget.attrs.update({'placeholder': 'Enter Email.'})
            if name == 'username':
                field.widget.attrs.update({'placeholder': 'Enter Username.'})
            if name == 'password1':
                field.widget.attrs.update({'placeholder': 'Enter Password.'})
            if name == 'password2':
                field.widget.attrs.update({'placeholder': 'Confirm Password.'})


class UpdateAccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name',  'email',
                  'discord_link', 'rank', 'division', 'profile_img']
        labels = {'discord_link': 'Discord',
                  'profile_img' : 'Profile Image',
                  'rank' : 'Rank'}

    def __init__(self, *args, **kwargs):
        super(UpdateAccountForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta():
        model = Message
        fields = ['subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if name == 'subject':
                field.widget.attrs.update({'placeholder': 'Enter Subject.'})
            if name == 'body':
                field.widget.attrs.update({'placeholder': 'Enter message here.'})
