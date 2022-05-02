from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Burgers/index.html')

def get_category(request, slug):
    return render(request, 'Burgers/category.html')