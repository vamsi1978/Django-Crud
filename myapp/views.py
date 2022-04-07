from ast import keyword
from cgitb import html, text
from email import message
from itertools import count
from os import uname
from unicodedata import name
from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .forms import ContentForm, RegistrationForm
from .models import User,Content
from django.db.models import Q

def indexfunction(request):
    return HttpResponse("My First Django Application")

def userfunction(request):
    return HttpResponse("My First Django Application.This is user function")

def guestfunction(request):
    return HttpResponse("My First Django Application.This is guest function")
def userfunction1(request,id):
    return HttpResponse(id)
def addfunction(request,id1,id2):
    return HttpResponse(id1+id2)
def userfunction2(request,name):
    return HttpResponse(name)
def userfunction3(request,id,name):
    mydict = {
        "id":id,
        "name":name
    }
    return JsonResponse(mydict)
def indexfunction1(request):
    return HttpResponse("<h3 align=center>Index Page</h3>")
#def userpage(request):
#   return redirect("user")

#myapp
def index(request):
    return render(request,"index.html")
def adminlogin(request):
    return render(request,"adminlogin.html")
def contactuspage(request):
    return render(request,"contactus.html")
def userlogin(request):
    return render(request,"userlogin.html")
def checkadmin(request):
    if request.method == "POST":
        aid=request.POST['aid']
        apwd=request.POST['apwd']
        if aid == "admin" and apwd == "admin":
            return redirect('adminhome')
        else:
            return HttpResponse("Login Invalid") 
def userreg(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save() #all values in form will be saved to table
            return redirect('userlogin')
    else:
        form = RegistrationForm()
        return render(request,'userreg.html',{'form':form})

def adminhome(request):
    return render(request,"adminhome.html")
def viewusers(request):
    users=User.objects.all() #select *from table
    count=User.objects.all().count()
    return  render(request,"viewusers.html",{'users':users,"count":count})
def alogout(request):
    return render(request,"adminlogin.html")
def deleteuser(request,id):
    User.objects.filter(id=id).delete()
    users=User.objects.all()
    count=User.objects.all().count()
    return  render(request,"viewusers.html",{'users':users,"count":count})
def checkuser(request):
     if request.method == "POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd'] 
        flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=pwd)) #this will return boolean value
        if flag:
            request.session['uname'] = uname #creating session variable
            return redirect("userhome")
        else:
            return HttpResponse("Login Invalid")
     else:
         return render("userlogin.html")
     return render("userlogin.html")

def userhome(request):
    uname=request.session['uname'] #retriving session variable
    return render(request,"userhome.html",{"uname":uname})
def changepwd(request):
    uname=request.session['uname'] 
    return render(request,"changepwd.html",{"uname":uname})
def ulogout(request):
    return render(request,"userlogin.html")
def changepwd1(request):
    uname=request.session['uname']
    if request.method == "POST":
        opwd=request.POST['opwd']
        npwd=request.POST['npwd']
        flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=opwd))
        if flag:
            User.objects.filter(username=uname).update(password=npwd)
            return HttpResponse("pwd is changed")
        else:
            return HttpResponse("old pwd is incorrect")
    else:
        return render("changepwd.html")
    return render("changepwd.html")
def deleteuserbyid(request):
    users=User.objects.all()
    return render(request,"deleteuserbyid.html",{"users":users})
def deleteuserbyid1(request):
    users=User.objects.all()
    if request.method=="POST":
        uid = request.POST["uid"]
        User.objects.filter(id=uid).delete()
        users = User.objects.all()
        count=User.objects.all().count()
        return render(request,"viewusers.html",{"users":users,"count":count})
    else:
        users=User.objects.all()
        return render(request,"deleteuserbyid.html",{"users":users})
    return render(request,"deleteuserbyid.html",{"users":users})
def addcontent(request):
    if request.method == 'POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            form.save() #all values in form will be saved to table
            return redirect('addcontent')
    else:
        form = ContentForm()
        return render(request,'addcontent.html',{'form':form})
    return render(request,'addcontent.html',{'form':form})
def searchcontent(request):
    uname=request.session['uname']
    return render(request,"searchcontent.html",{"uname":uname})
def searchcontent1(request):
    uname=request.session['uname']
    if request.method == "POST":
        appu=request.POST['appu']
        flag=Content.objects.filter(Q(title__icontains=appu))
        if flag:
            content=Content.objects.filter(Q(title__contains=appu))
            count=Content.objects.filter(Q(title__contains=appu)).count()
            return render(request,"displaycontent.html",{"content":content,"uname":uname,"count":count})
        else:
            return HttpResponse("Search not Found")
    else:
        return render(request,"searchcontent.html")
    return render(request,"searchcontent.html")
def viewcontent(request):
    contents=Content.objects.all()
    count=Content.objects.all().count()
    return render(request,"viewcontent.html",{"contents":contents,"count":count})
