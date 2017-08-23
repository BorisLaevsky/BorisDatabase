# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Worker, Company, Contracts


admin.site.register(Worker)
admin.site.register(Company)
admin.site.register(Contracts)
