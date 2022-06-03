from django.shortcuts import redirect, render
from .forms import Postform

def home(request):
    return render(request, 'index.html')

def postcreate(request):
    # request method가 POST일 경우 입력값 저장하고, GET 일 경우 form 입력 html 띄우기
    if request.method == 'POST' or request.method == 'FILES':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Postform()
    return render(request, 'post_form.html', {'form': form})