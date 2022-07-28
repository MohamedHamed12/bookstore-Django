# from sre_constants import CATEGORY
# from asyncio.windows_events import NULL
# from unicodedata import name
# from pyexpat import model
# from tkinter import N
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# class Customer(models.Model):
#     namee=models.CharField(max_length=15,null=True)


class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    namee = models.CharField(max_length=50, null=True)
    age = models.CharField(max_length=15, null=True)

    data_create = models.DateTimeField(auto_now_add=True, null=True)
    avatar=models.ImageField(blank=True, default='s.png')

    def __str__(self):
        return self.namee
class tag(models.Model):
    nname=models.CharField( max_length=50,null=True)
    def __str__(self) :
        return self.nname

class book(models.Model):
    CCATEGORY = (
        ('commic', 'commic'),
        ('fan', 'fan'),
        ('sci', 'sci')
    )
    namee = models.CharField(max_length=30, null=True)
    price = models.FloatField(null=True)
    discrib = models.CharField(max_length=200, null=True)
    data_create = models.DateTimeField(auto_now_add=True, null=True)
    t=models.ManyToManyField(tag)
    # def __str__(self) -> str:
    #      return super().__str__()

    def __str__(self):
        return self.namee



class order(models.Model):
    ssstatus = (
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('in progress', 'inprograss')
    )
    cus = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    b = models.ForeignKey(book, null=True, on_delete=models.SET_NULL)
    t=models.ManyToManyField(tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    sstatus = models.CharField(max_length=200, null=True, choices=ssstatus)
    # data_created=models.DataTimefield(auto_now_add=True,null=True)
# Create your models here.
