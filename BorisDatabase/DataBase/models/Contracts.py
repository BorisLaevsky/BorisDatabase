from __future__ import unicode_literals

from django.db import models

from .Worker import Worker
from .Company import Company
from .Pay import Pay
# Create your models here.

class Contracts(models.Model):
    worker = models.ForeignKey(Worker)
    role = models.ForeignKey(Pay)
    hours = models.IntegerField()

