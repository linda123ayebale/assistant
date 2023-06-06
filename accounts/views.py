from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.

def loginViews(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("chatbot:home")
        else:
            messages.error(request, 'Oops, Invalid Username or Password.try again')

    return render(request, 'accounts/login.html')


def registerViews(request):
    form = CustomUserCreationForm()

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def forgotViews(request):
    return render(request, 'accounts/forgot.html')


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')