from django.db import models
from PIL import  Image, ImageDraw
# Create your models here.

class Home(models.Model):
    banner_title = models.CharField(max_length = 64)
    banner_details  = models.TextField()
    detail_heading = models.CharField(max_length = 64)
    details = models.TextField()
    image = models.ImageField(upload_to='webpic/', null=True)

    def __str__(self):
        return self.banner_title

class aboutUs(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    history_title = models.CharField(max_length=64)
    history_description = models.TextField()
    image = models.ImageField(upload_to='aboutus', null=True)

    def __str__(self):
        return self.title 

class ContactUs(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    address  = models.TextField()
    mobile = models.CharField(max_length = 64, null=True)
    email = models.CharField(max_length = 64, null=True)
    facebook = models.CharField(max_length = 64, null=True)
    twitter = models.CharField(max_length = 64, null=True)
    instgram = models.CharField(max_length = 64, null=True)

    def __str__(self):
        return self.title


class ProductType(models.Model):
    name =models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    code = models.CharField(max_length=64)
    image = models.ImageField(upload_to='profile/', default='profile/default.png', null=True)
    producttype = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name


