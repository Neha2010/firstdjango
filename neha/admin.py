# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# the module name is app_name.models
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
from django.contrib import admin
from neha.models import reg

admin.site.register(reg)