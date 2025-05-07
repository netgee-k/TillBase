
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Tillbase!")

# Dashboard page view (new)
##def dashboard(request):
##  return HttpResponse("Welcome to your Dashboard!")

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})
