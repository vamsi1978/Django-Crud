import email
from os import link
from unicodedata import category
from django.db import models

# Create your models here.
class User(models.Model):
    fullname=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    mobileno=models.CharField(max_length=100,blank=False)
    location=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table = "user_table"

class Content(models.Model):
    category_choices = (('Education','Education'),('Programming','Programming'),('others','others'))
    category=models.CharField(max_length=100,choices=category_choices,blank=False)
    title=models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=1000,blank=False)
    link=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="content_table"