from django.shortcuts import render
from django.http import HttpResponse

def index(resquest):
    return HttpResponse("Hello Jorge Sev this is a test")


