from .models import Coach, Accomplishments
from django.forms import ModelForm


class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['display_name',
                  'headline',
                  'profile_img',
                  'body',
                  'discord_link']


    def __init__(self, *args, **kwargs):
        super(CoachForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'name':
                field.widget.attrs.update({'class':'input', 'placeholder':'Enter Display Name','maxlength': 50})
                continue
            if name == 'body':
                field.widget.attrs.update({'class':'input','placeholder':'Enter Description'})
                continue
            else:
                field.widget.attrs.update({'class':'input'})
            
class AccomplishmentForm(ModelForm):
    class Meta:
        model = Accomplishments
        fields = '__all__'
        exclude = ['owner']

        def __init__(self, *args, **kwargs):
            super(AccomplishmentForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input', 'placeholder':'Enter Accomplishment'})
