from .views import index,login
from django.urls import path

urlpatterns=[
        path('',index),
        path('login',login,name="login")        
        ]

