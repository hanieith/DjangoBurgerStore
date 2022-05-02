from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *

class Home(ListView):
    model = Post
    template_name = 'Burgers/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


def index(request):
    return render(request, 'Burgers/index.html')

def get_category(request, slug):
    return render(request, 'Burgers/category.html')

def get_post(request, slug):
    return render(request, 'Burgers/category.html')