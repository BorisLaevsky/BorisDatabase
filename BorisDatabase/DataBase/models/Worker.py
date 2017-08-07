# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Worker(models.Model):
    worker_id = models.IntegerField()
    full_name = models.CharField(max_length=200)
    workers_contacts = models.CharField(max_length=200)
