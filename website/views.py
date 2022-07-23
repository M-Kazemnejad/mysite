from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return HttpResponse('this is home')

def contact_view(request):
    return HttpResponse('this is contact')

def about_view(request):
    return HttpResponse('this is about')