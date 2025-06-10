from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Aptitude Test API is running.")
