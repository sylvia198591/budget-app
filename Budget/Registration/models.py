from django.db import models
from datetime import *
# from datetime.date.today()
# from django.utils import *
# from django.contrib import admin
# from django.conf import settings
# from django.utils.translation import *
# from django.utils.translation import gettext_lazy as _
# from django.utils import timezone

# Create your models here.
class udtl(models.Model):
    # uid=models.CharField(max_length=120,unique=True)
    name=models.CharField(max_length=200)
    tel=models.IntegerField()
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    isActive=models.BooleanField(default=False)
    # acdate=models.DateField()
    # addate = models.DateField()
    # isLog=models.BooleanField(default=False)
    # lcdate = models.DateTimeField(auto_now=True,default=False)
    # lddate = models.DateTimeField(auto_now=True,default=False)

    def __str__(self):
        return self.username


class Account(models.Model):
    paymode=models.CharField(max_length=250)
    user=models.CharField(max_length=250,)

    def __str__(self):
        return self.paymode


class Essential(models.Model):
    category=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.category


class Entry(models.Model):
    # class Type(models.TextChoices):
    #     EXPENSE= 'E', _('Expense')
    #     INCOME = 'I', _('Income')
    # uid=models.ForeignKey(Registration,on_delete=models.CASCADE)
    username=models.ForeignKey(udtl,on_delete=models.CASCADE)
    paymode=models.ForeignKey(Account,on_delete=models.CASCADE)
    category=models.ForeignKey(Essential,on_delete=models.CASCADE)
    amount=models.FloatField()
    # type=models.CharField(max_length=1,choices=Type.choices,
    #                       default=Type.EXPENSE,)
    # dfield=models.DateField(default=date.today())
    dfield = models.DateField()
    # image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.amount








    # image=models.ImageField(upload_to='images/')
    # def __str__(self):
    #     return self.item_name