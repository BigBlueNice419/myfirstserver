from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from random import randint

def index(request):
    return HttpResponse("Hello, CSC630!", content_type="text/plain")

def personal(request, some_name):
    return HttpResponse("<h2> Hello, " + some_name + " </h2>")

def random(request):
    return JsonResponse({'number' : randint(0, 1000000000)})    
