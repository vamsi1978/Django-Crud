from django.shortcuts import render
from django.http import HttpResponse

def demofunction(request):
    return HttpResponse("My First Django Application.This is in project folder")
def mainpage(request):
    return render(request,"project.html")