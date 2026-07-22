from django.urls import path
from .views import *

urlpatterns=[
    path("welcome_app/",welcome_app,name="welcome_app"),
        path('home/',home,name="home"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact")
    
]