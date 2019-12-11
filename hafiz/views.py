from django.shortcuts import redirect, render
from desktop.models import Product
from django.http import HttpResponse, JsonResponse
def index(request):
    context = {}
    template_name = 'index.html'
    obj = Product.objects.all()
    obj = list(obj.values('id','name','description','image', 'code'))
    context = { 'data': obj }
    return render(request,template_name, context)

import json
def index_type(request, post_type = None):
    template_name = 'products.html'
    if post_type == 'all':
        obj = Product.objects.all()
    else:
        obj = Product.objects.filter(producttype__name = post_type)        
    
    obj = list(obj.values('id','name','description','image', 'code'))
    # data = json.dumps({ "error": '', "data": obj })
    # context = { "data" : obj }
    return render(request, "products.html", { "data" : obj })
    # return HttpResponse(json.dumps({ "error": '', "data": obj }), content_type='application/json')

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
