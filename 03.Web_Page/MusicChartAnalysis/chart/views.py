from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def genre(request):
    return render(request, 'genre.html')

def singer(request):
    return render(request, 'singer.html')

def title(request):
    return render(request, 'title.html')