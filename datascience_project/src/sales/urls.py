from django.urls import path
from .views import (SalesListView, home_view, SalesDetailView)

app_name = 'sales'

urlpatterns = [

  path('',home_view,name='home'),
  path('list/',SalesListView.as_view(),name ='list'),
  path('list/<pk>/',SalesDetailView.as_view(),name ='detail'),
    
]
