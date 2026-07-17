from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse("<h1>Atharva Ramesh Deshmukh<h1>")

def index(request):
    return render(request,"index.html")