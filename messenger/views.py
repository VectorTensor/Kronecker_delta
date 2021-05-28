from django.shortcuts import render
from .models import Messages 
from Question.views import login
# Create your views here.
username='Anonymous'
def ShowMessenger(request):
    print('In ShowMessenger')
    if request.method == 'POST':
        global username
        data=request.POST
        passw=data['pass']
        username=data['Name']
        if passw=="naruto":
            return render(request,'messenger/index.html')
        else:
            return render(request,'Question/login.html')

    else:
        return render(request,'Question/login.html')


def Postdata(request):
    if request.method =='POST':
        data=request.POST
        print(data)
        Entry=Messages.objects.create(Message=data['name'],User=username)
        return render(request,'messenger/index.html')
