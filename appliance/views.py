from django.contrib import auth
from django.shortcuts import redirect, render
from .forms import ApplyForm


def home(request): # home.html 보여줌
    return render(request, 'home.html')


def apply(request):  # 지원서 html
    return render(request, 'apply.html')


def create(request): # 지원서 입력 받은 후 저장
    if request.method == 'POST':
        # 입력내용 db에 저장
        form = ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplyForm()
    return render(request, 'apply.html', {'form': form})