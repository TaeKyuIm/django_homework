from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'login.html')
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            new_user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'])
            auth.login(request, new_user)
            return redirect('home')
    return render(request, 'signup.html')