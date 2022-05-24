from django import forms
from .models import Apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'id', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5']