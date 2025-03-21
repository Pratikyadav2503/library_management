from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to the Library Management System!")

urlpatterns = [
    path("", home),  # This handles requests to "/"
    path("api/", include("library.urls")),
]
