from tkinter.messagebox import NO
from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # request == POST 면 로그인
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None: # 실제 존재하는 회원이면
            auth.login(request, user)
            return redirect('home')
        
        else:
            return render(request, 'bad_login.html')
        
    # request == GET 이면 html 띄우기
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, new_user)
            return redirect('home')
    return render(request, 'register.html')