from django.shortcuts import redirect, render
from desktop.models import Product, Home, aboutUs, ContactUs
from django.http import HttpResponse, JsonResponse
import json
from django.core.paginator import Paginator


def index(request):
    context = {}
    template_name = 'index.html'
    obj = Product.objects.all()
    home_items = Home.objects.all()
    home_items = list(home_items.values('banner_title','banner_details','detail_heading','details','image'))
    home_items = home_items[0];
    obj = list(obj.values('id','name','description','image', 'code'))
    paginator = Paginator(obj, 8)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request,template_name, { 'data': contacts , 'home': home_items})



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
    obj = aboutUs.objects.all()
    obj = list(obj.values('title','description','history_title','history_description','image'))
    obj = obj[0]
    return render(request,template_name,{'data': obj})

def contact(request):
    template_name = 'contact.html'
    obj = ContactUs.objects.all()
    obj = list(obj.values('title','description','address','mobile','email','facebook','twitter','instgram','map'))
    obj = obj[0]

    return render(request,template_name,{'data': obj})

def detail(request, id):
    template_name = 'detail.html'
    if id:
        obj = Product.objects.filter(id=id)
        obj = list(obj.values('id','name','description','code','image'))
        obj_all = Product.objects.all().order_by('-id')[:4]
        obj_all = list(obj_all.values('id','name','description','image', 'code'))
        # obj_all = Paginator(obj_all, 8)
        return render(request,template_name, {'single_data': obj[0], 'data': obj_all})
