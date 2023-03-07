from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dilip(request):
    return HttpResponse('<marquee><h1>dilip is a handsome boy</h1><marquee>')

def chitti(request):
    return HttpResponse('chitti is a lazy fellow')
