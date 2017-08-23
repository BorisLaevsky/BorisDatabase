# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Worker, Company
from .forms import AddWorkerForm, SearchWorkerForm, LoginForm, SearchCompanyForm, AddCompanyForm
from django.contrib.auth import authenticate, login

def login_page(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('main_page')
            else:
                return HttpResponseRedirect('')
    else:
        login_form = LoginForm()
    return  render(request, 'DataBase/login_page.html', {'login_form': login_form, })


def main_page(request):
    if request.user.is_authenticated():
        list_of_workers = Worker.objects.order_by('-full_name')
        if request.method == 'POST':
            search_form = SearchWorkerForm(request.POST)
            if search_form.is_valid():
                return HttpResponseRedirect(request.POST.get('passport_number'))
        else:
            search_form = SearchWorkerForm()
        return render(request, 'DataBase/main_page.html', {'list_of_workers': list_of_workers,
                                                           'search_form': search_form, })
    else:
        return HttpResponseRedirect('/database_app/')


def worker(request):
    if request.user.is_authenticated():
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
                return HttpResponseRedirect('')
            if search_form.is_valid():
                return HttpResponseRedirect('/database_app/main_page/' + request.POST.get('passport_number'))
        else:
            form = AddWorkerForm()
            search_form = SearchWorkerForm()
        return render(request, 'DataBase/worker_page.html', {'list_of_workers': list_of_workers,
                                                       'AddWorker_form': form,
                                                       'search_form': search_form, })
    else:
        return HttpResponseRedirect('/database_app/')


def find_worker(request, worker_passport_number):
    if request.user.is_authenticated():
        worker_info = Worker.objects.filter(passport_number__contains = worker_passport_number)
        return render(request, 'DataBase/find_worker.html', {'worker_info': worker_info, })
    else:
        return HttpResponseRedirect('/database_app/')


def company(request):
    if request.user.is_authenticated():
        list_of_companies = Company.objects.order_by('-company_name')
        if request.method == 'POST':
            form = AddCompanyForm(request.POST)
            search_form = SearchCompanyForm(request.POST)
            if form.is_valid():
                new_company = Company(
                    company_name=request.POST.get('company_name'),
                    company_contact=request.POST.get('company_contact'),
                    company_adress=request.POST.get('company_adress')
                )
                new_company.save()
                return HttpResponseRedirect('')
            if search_form.is_valid():
                return HttpResponseRedirect('/database_app/main_page/company/' + request.POST.get('company_name'))
        else:
            form = AddCompanyForm()
            search_form = SearchCompanyForm()
        return render(request, 'DataBase/company_page.html', {'list_of_companies': list_of_companies,
                                                              'AddCompany_form': form,
                                                              'search_form': search_form, })
    else:
        return HttpResponseRedirect('/database_app/')


def find_company(request, company_name):
    if request.user.is_authenticated():
        company_info = Company.objects.filter(company_name__contains = company_name)
        return render(request, 'DataBase/find_company.html', {'company_info': company_info, })
    else:
        return HttpResponseRedirect('/database_app/')


def contracts(request):
    return HttpResponse('Contracts page')



