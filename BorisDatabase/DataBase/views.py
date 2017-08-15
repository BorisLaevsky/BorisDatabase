# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Worker
from django.urls import reverse
from .forms import AddWorkerForm


def main_page(request):
    list_of_workers = Worker.objects.order_by('-full_name')
    if request.method == 'POST':
        form = AddWorkerForm(request.POST)
        if form.is_valid():
            new_worker = Worker(
                passport_number = request.POST.get('passport_number'),
                full_name = request.POST.get('full_name'),
                workers_contacts = request.POST.get('workers_contacts')
            )
            new_worker.save()
            return HttpResponseRedirect('/database/')
    else:
        form = AddWorkerForm()
    return render(request, 'DataBase/main_page.html', {'list_of_workers': list_of_workers, 'AddWorker_form': form })


def worker(request):
    return HttpResponse("Worker page")

def company(request):
    return HttpResponse('Company page')

def contracts(request):
    return HttpResponse('Contracts page')
