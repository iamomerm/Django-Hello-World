from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'John Smith'})


def about(request):
    return HttpResponse('About Page', status=200)
