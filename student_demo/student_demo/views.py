from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
def index(request):
    context = {}
    return render(request, "index.html", context)

def login_request(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    if user is not None:
        login(request, user)
        return redirect(referer)
    else:
        return render(request, 'error.html', {'message': '用户名或密码不正确', 'redirect_to': referer})