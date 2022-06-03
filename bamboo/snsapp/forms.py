from django import forms
from .models import Post

class Postform(forms.ModelForm): # django의 ModelForm 이용
    class Meta:
        model = Post # 어느 모델을 이용할지 있음
        fields = '__all__'