from django.shortcuts import render
from .models import Messages 
# Create your views here.
username='Anonymous'
def ShowMessenger(request):
    
    return render(request,'messenger/index.html')

def Postdata(request):
    if request.method =='POST':
        data=request.POST
        print(data)
        Entry=Messages.objects.create(Message=data['name'],User=username)
        return render(request,'messenger/index.html')
