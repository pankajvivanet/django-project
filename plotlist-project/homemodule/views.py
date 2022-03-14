from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

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