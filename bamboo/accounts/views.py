from django.shortcuts import render

def login(request):
    # request == POST 면 로그인
    if request.method == 'POST':
        pass
    # request == GET 이면 html 띄우기
    else:
        return render(request, 'login.html')