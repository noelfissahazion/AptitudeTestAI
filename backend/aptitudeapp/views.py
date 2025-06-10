from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Aptitude Test API is running.")

# This is a placeholder view function that can be replaced with actual logic later.