from django.shortcuts import redirect, render
from desktop.models import Product
from django.http import HttpResponse, JsonResponse
import json
from django.core.paginator import Paginator


def index(request):
    context = {}
    template_name = 'index.html'
    obj = Product.objects.all()
    obj = list(obj.values('id','name','description','image', 'code'))
    paginator = Paginator(obj, 8)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request,template_name, { 'data': contacts })



def index_type(request, post_type = None):
    template_name = 'products.html'
    if post_type == 'all':
        obj = Product.objects.all()
    else:
        obj = Product.objects.filter(producttype__name = post_type)
    obj = list(obj.values('id','name','description','image', 'code'))
    paginator = Paginator(obj, 8)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, "products.html", { "data" : contacts })

def design(request):
    context = {}
    template_name = 'design.html'
    obj = Product.objects.all()
    obj = list(obj.values('id','name','description','image', 'code'))
    # paginator = Paginator(obj, 8)
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    return render(request,template_name, { 'data': obj })

def about(request):
    template_name = 'about.html'
    return render(request,template_name)

def contact(request):
    template_name = 'contact.html'
    return render(request,template_name)

def detail(request, id):
    template_name = 'detail.html'
    if id:
        obj = Product.objects.filter(id=id)
        obj = list(obj.values('id','name','description','code','image'))
        context = {'data': obj[0]}
        return render(request,template_name, context)
