from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h1>Hello <br> My self Atharva Ramesh Deshmukh</h1>")