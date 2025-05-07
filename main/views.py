from django.shortcuts import render

# Create your views here.
#homeview
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Tillbase!")

# Dashboard page view (new)
def dashboard(request):
    return HttpResponse("Welcome to your Dashboard!")
