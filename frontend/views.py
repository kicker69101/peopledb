from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html')


def people(request):
    return render(request, 'people/person.html')
