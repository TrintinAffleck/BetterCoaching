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
            field.widget.attrs.update({'class': 'input'})


class UpdateAccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email',
                  'discord_link', 'rank', 'division']
        labels = {'discord_link': 'Discord'}


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