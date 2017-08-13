# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Worker
from django.urls import reverse

def main_page(request):
    list_of_workers = Worker.objects.order_by('-full_name')
    context = {
        'list_of_workers': list_of_workers,
    }
    if request.method == 'POST' and request.POST.get('full_name', False):
        new_worker = Worker(passport_number = 0,full_name = '',workers_contacts = '')
        new_worker.passport_number = request.POST.get('passport_number', False)
        new_worker.full_name = request.POST.get('full_name', False)
        new_worker.workers_contacts = request.POST.get('workers_contacts', False)
        new_worker.save()
        return HttpResponseRedirect('/database/')
    else:
        return render(request, 'DataBase/main_page.html', context)

def worker(request):
    return HttpResponse("Worker page")

def company(request):
    return HttpResponse('Company page')

def contracts(request):
    return HttpResponse('Contracts page')
