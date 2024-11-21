from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def views_home(request:HttpRequest):
    return render(request ,'main/home.html')
def create_views(request:HttpRequest):
    if
    return render(request , 'main/create.html')