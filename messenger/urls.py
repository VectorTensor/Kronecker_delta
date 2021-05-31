from django.urls import path

from .views import ShowMessenger,Postdata
app_name="Mess"
urlpatterns=[
        path('',ShowMessenger,name='Messenger'),
        path('poster',Postdata,name='poster')
        ]
