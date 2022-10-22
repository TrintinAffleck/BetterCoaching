from .models import Coach
from django.forms import ModelForm

class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'body', 'rank']