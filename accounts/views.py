from django.shortcuts import render, redirect
from django.contrib import auth
from accounts.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login

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
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = UserForm()
    return render(request, 'signup.html')