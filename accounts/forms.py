from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        
    def save(self, commit = True):
        user = super(UserForm, self).save(commit=True)
        user.email = self.data['email']
        if commit:
            user.save()
        return user