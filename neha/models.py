# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models


class reg(models.Model):
    name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50, primary_key=True)
    phone = models.CharField(max_length=50,blank=False)
    password = models.CharField(max_length=32, blank=False)
    repassword= models.CharField(max_length=32,blank=False)





    def __str__(self):
        return self.email # returns email when reg.objects.all() is called
