from django.urls import path

from .views import ShowMessenger
urlpatterns=[
        path('',ShowMessenger,name='Messenger')
        ]
print("Hello")
