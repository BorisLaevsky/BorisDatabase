# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Worker(models.Model):
    passport_number = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    workers_contacts = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
