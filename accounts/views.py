from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def loginViews(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("chatbot:home")

    return render(request, 'accounts/login.html')


def registerViews(request):
    return render(request, 'accounts/register.html')





def forgotViews(request):
    return render(request, 'accounts/forgot.html')
