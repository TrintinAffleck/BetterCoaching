from .models import Coach, Rank
from django.forms import ModelForm


class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['name',
                  'headline',
                  'profile_img',
                  'rank',
                  'body']


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
            
            
