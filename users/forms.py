from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Select
from .models import Profile
from coaches.models import Coach, Rank

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'first_name','email','username','password1','password2',
        ]
        labels = {'first_name' : 'Name'}

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class UpdateAccountForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username','email','discord_link']
        labels = {'discord_link': 'Discord'}


class UpdateCoachForm(UpdateAccountForm):
    class Meta:
        model = Coach
        fields = ['display_name', 'headline', 'body', 'rank',
                  'discord_link', 'profile_img']
                  
        labels = {'discord_link': 'Discord',
                  'profile_img' : 'Profile Image',
                  'display_name': 'Display Name',
                  'headline' : 'Headline',
                  'body' : 'Description/Bio',
                  'rank' : 'Current Rank'
                  }
        widgets = {'rank' : Select(choices=Rank.RANKS) }

    def __init__(self, *args, **kwargs):
        super(UpdateCoachForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
