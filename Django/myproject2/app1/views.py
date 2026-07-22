from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_app(request):
    return HttpResponse("<h1>Welcome to app1</h1>")

def home(request):
    return render(request,"app1\\home.html")

def about(request):
    return render(request,'app1\\about.html')

def contact(request):
    return render(request,"app1\\contact.html")



