from unicodedata import name
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('demo',views.demofunction,name="demo"),
    path('main',views.mainpage,name="main")
]
