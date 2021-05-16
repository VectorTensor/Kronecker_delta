from django.shortcuts import render

# Create your views here.
def ShowMessenger(request):
    return render(request,'messenger/index.html')

