from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homeviews(request):
    return HttpResponse("Hello, this is chartbot!")
