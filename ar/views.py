from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def homeviews(request):
    return render(request, "ar/index.html")
