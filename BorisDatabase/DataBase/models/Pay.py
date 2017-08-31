from __future__ import unicode_literals

from django.db import models
from .Company import Company
# Create your models here.

class Pay(models.Model):
    company = models.ForeignKey(Company, related_name='company')
    role = models.CharField(max_length=200)
    pay = models.CharField(max_length=200)
