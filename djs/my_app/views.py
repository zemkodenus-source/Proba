from django.shortcuts import render
from django.http import HttpResponse
from .list_products import catalog_cars

def index(request):
    return render(request , 'my_app/index.html')

def about(request):
    return render(request , 'my_app/about.html')

def catalog(request):
    catalog_p = {
        'value' : [ 'BMW' , 'AUDI' , 'FORD' ,catalog_cars ] ,
        'for_example' : 'Some example'
    }
    return render(request, 'my_app/catalog.html' , catalog_p)
