from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'hello.html',{'name' : "Sid"})

def add(request):
    val1 = int(request.GET["value1"])
    val2 = int(request.GET["value2"])
    res = val1 + val2
    return render(request,"result.html",{'addittion':res})