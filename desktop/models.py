from django.db import models
from PIL import  Image, ImageDraw
# Create your models here.

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

