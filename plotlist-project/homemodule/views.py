from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request
#response
#action handler / request handler

def welcome(request):
    return HttpResponse("Welcome to Plotlist")
