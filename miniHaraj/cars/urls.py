from django.urls import path
from . import views

urlpatterns = [
  path('',views.views_home,name='views_home')  
]