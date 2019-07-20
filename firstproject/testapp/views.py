from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def timeinfo(request):
    msg = "<h1>Hello Friends Very Good Morning !!!!!</h1><hr>"
    msg = msg+str(datetime.datetime.now())
    return HttpResponse(msg)
