from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manu(request):
    return HttpResponse('This a Sample String')