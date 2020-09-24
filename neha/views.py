# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from neha.forms import RegForm
from neha.models import reg
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    #print("submitted")
    form = RegForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'base.html', context)
    #return render(request, "base.html")


def header(request):
    return render(request , "header.html")

def login(request):
    fm = RegForm(request.POST or None)
    if fm.is_valid():
        fm.save()


    context = {'form': fm}

    return render(request, 'login.html', context)


def afterlogin(request):
    data = request.POST.get('email')
    obj = reg.objects.filter(email=data).values()
    context = {'data': obj}
    return render(request, 'afterlogin.html',context)



def clean(self):
    cleaned_data = super(RegForm, self).clean()

    password = cleaned_data.get('password')
    password_confirm = cleaned_data.get('repassword ')

    if password and re_password:
        if password != re_password:
            raise forms.ValidationError("The two password fields must match.")
    return cleaned_data