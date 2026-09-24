from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse

def bweb(request):
    return HttpResponse("Hello, this is the bweb view.完成")

def aweb(request):
    return HttpResponse("Hello, this is the aweb view.完成")
