from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from homemodule.models import CityName, AreaNames

# Create your views here.
#request
#response
#action handler / request handler

def welcome(request):
    return HttpResponse("Welcome to Plotlist")

def redirectURL(request):
    return redirect("https://google.com")

def acceptInput(request, inputText):
    text = "Todat is = %s"%inputText
    return HttpResponse(text)

def templateHTML(request):
    return render(request, 'welcome.html', {'name' : 'John'})

def show(request):
    citynames = CityName.objects.all()
    areanames = AreaNames.objects.all()
    return render(request, 'show.html', {'CityName': citynames, "AreaNames":areanames})