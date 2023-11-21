from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class Catagory(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self. name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=HTMLField()
    image=models.ImageField(upload_to="image",null=True)
    type=models.ForeignKey( Catagory, on_delete=models.CASCADE,)
    price=models.IntegerField()
    def __str__(self):
        return self. name
    
    
    
    
    
    
