from unicodedata import name
from django.urls import path 
from myapp import views

urlpatterns = [
    #path('',views.indexfunction,name="index"),   
    #path('user',views.userfunction,name="user"), 
    path('guest',views.guestfunction,name="guest"), 
    path('user/<int:id>',views.userfunction1,name="user_1"),
    path('user/<int:id1>/<int:id2>',views.addfunction,name="add"),
    path('user/<str:name>',views.userfunction2,name="user_2"),
    path('user/<int:id>/<str:name>',views.userfunction3,name="user_3"),
    #path('index',views.indexfunction1,name="index1"),
    #path('userpage',views.userpage,name="userpage"),

    #app urls
    path('',views.index,name="index"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('contactus',views.contactuspage,name="contactuspage"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('userreg',views.userreg,name="userreg"),
    path('checkadmin',views.checkadmin,name="checkadmin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('viewusers',views.viewusers,name="viewusers"),
    path('alogout',views.alogout,name="alogout"),
    path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
    path('checkuser',views.checkuser,name="checkuser"),
    path('userhome',views.userhome,name="userhome"),
    path('changepwd',views.changepwd,name="changepwd"),
    path('ulogout',views.ulogout,name="ulogout"),
    path('changepwd1',views.changepwd1,name="changepwd1"),
    path('deleteuserbyid',views.deleteuserbyid,name="deleteuserbyid"),
    path('deleteuserbyid1',views.deleteuserbyid1,name="deleteuserbyid1"),
    path('addcontent',views.addcontent,name="addcontent"),
    path('searchcontent',views.searchcontent,name="searchcontent"),
    path('searchcontent1',views.searchcontent1,name="searchcontent1"),
    path('viewcontent',views.viewcontent,name="viewcontent"),
]