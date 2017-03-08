from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import *


# Create your views here.
@csrf_protect
def login(request):
    '''
    login
    '''
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print("User Login:  Username:" + username + '    Password:' + password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        ctx = {}
        return render(request, 'login.html')



def logout(request):
    '''
    logout
    URL: /users/logout
    '''
    logout(request)
    return redirect('/')
