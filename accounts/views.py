from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.

def loginViews(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    return render(request, 'accounts/login.html')


def registerViews(request):
    return render(request, 'accounts/register.html')





def forgotViews(request):
    return render(request, 'accounts/forgot.html')
