# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_adress = models.CharField(max_length=200)
    company_contact = models.CharField(max_length=200)

    def __str__(self):
        return str(self.company_name)+str(self.company_adress)
