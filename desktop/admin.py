from django.contrib import admin
from desktop.models import Product,ProductType, Home, aboutUs, ContactUs
# Register your models here.

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Home)
admin.site.register(aboutUs)
admin.site.register(ContactUs)
