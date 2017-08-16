# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Worker
from .forms import AddWorkerForm, SearchWorkerForm


def main_page(request):
    list_of_workers = Worker.objects.order_by('-full_name')
    if request.method == 'POST':
        form = AddWorkerForm(request.POST)
        search_form = SearchWorkerForm(request.POST)
        if form.is_valid():
            new_worker = Worker(
                passport_number=request.POST.get('passport_number'),
                full_name=request.POST.get('full_name'),
                workers_contacts=request.POST.get('workers_contacts')
            )
            new_worker.save()
            return HttpResponseRedirect('/database/')
        if search_form.is_valid():
            return HttpResponseRedirect(request.POST.get('passport_number'))
    else:
        form = AddWorkerForm()
        search_form = SearchWorkerForm()
    return render(request, 'DataBase/main_page.html', {'list_of_workers': list_of_workers,
                                                       'AddWorker_form': form,
                                                       'search_form': search_form, })


def worker(request):
    return HttpResponse("Worker page")


def find_worker(request, worker_passport_number):
    worker_info = Worker.objects.filter(passport_number__contains = worker_passport_number)
    return render(request, 'DataBase/find_worker.html', {'worker_info': worker_info, })


def company(request):
    return HttpResponse('Company page')

def contracts(request):
    return HttpResponse('Contracts page')
