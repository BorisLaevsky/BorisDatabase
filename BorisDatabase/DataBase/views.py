# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def main_page(request):
    template = loader.get_template('DataBase/main_page.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def worker(request):
    return HttpResponse("Worker page")

def company(request):
    return HttpResponse('Company page')

def contracts(request):
    return HttpResponse('Contracts page')
