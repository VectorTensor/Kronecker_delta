from django.urls import path

from .views import ShowMessenger,Postdata
urlpatterns=[
        path('',ShowMessenger,name='Messenger'),
        path('poster',Postdata,name='poster')
        ]
