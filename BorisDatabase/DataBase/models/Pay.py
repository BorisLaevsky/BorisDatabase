from __future__ import unicode_literals

from django.db import models
from .Worker import Worker
from .Company import Company
# Create your models here.

class Pay(models.Model):
    worker = models.ForeignKey(Worker)
    company = models.ForeignKey(Company)
    role = models.CharField(max_length=200)
    pay = models.CharField(max_length=200)
