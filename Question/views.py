from django.shortcuts import render
from .models import Questions
# Create your views here.

def index(request):

    return render(request,'Question/index.html')

def login(request):
    return render(request,'Question/login.html')
