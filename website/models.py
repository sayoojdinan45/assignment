from typing import DefaultDict
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models

# Create your models here.
class SignUp(models.Model):
    Name=models.CharField(max_length=10,default='')
    Designation=models.CharField(max_length=20,default='')
    Email=models.EmailField(default='')
    Password=models.CharField(max_length=8,default='')
    Pic=models.ImageField(default='')
    Phone=models.IntegerField(default='')
class ProductTable(models.Model):
    Product_Name=models.CharField(max_length=20,default='')
    Model=models.CharField(max_length=10,default='')
    Price=models.IntegerField(default='')
    color=models.CharField(max_length=10,default='')
    image=models.ImageField(default='')
