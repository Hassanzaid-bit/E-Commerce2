from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User

LAPTOP_TYPE = [
    ("Laptop/Notenook", "Laptop/Notenook"),
    ("2 in 1", "2 in 1"),
    ("Chromebook", "Chromebook"),
    ("Microsoft Surface", "Microsoft Surface")
]

DESKTOP_TYPE = [
    ("Desktop", "Desktop"),
    ("All-in-one", "All-in-one")
]

BRANDS = [
    ("Acer", "Acer"), 
    ("ASUS", "ASUS"), 
    ("HP", "HP"), 
    ("DELL", "DELL"), 
    ("MICROSOFT", "MICROSOFT"), 
    ("LENOVO", "LENOVO")
]

MEMORY = [
    ("4GB", "4GB"),
    ("8GB", "8GB"),
    ("16GB","16GB")
]

PROCESSOR = [
    ("Intel", (
        ("core i9", "core i9"),
        ("core i7", "core i7"),
        ("core i5", "core i5"),
        ("core i3", "core i3"),
        ("other", "other"))
    ),
    ("AMD", (
        ("Ryzen 7", "Ryzen 7"),
        ("Ryzen 5", "Ryzen 5"),
        ("Ryzen 3", "Ryzen 3"),
        ("Other", "Other"))
    )
]


# Create your models here.
class Computer(PolymorphicModel):
    pass
      

class Portable(Computer):
    Brand = models.CharField(max_length=200, choices= BRANDS,default="HP")
    series = models.CharField(max_length=200, blank=True)
    model = models.CharField(max_length=200,  default="")
    slug = models.SlugField(max_length=200, db_index=True)
    type = models.CharField(max_length=200,choices=LAPTOP_TYPE, default="Laptop type")
    memory = models.CharField(max_length=200, choices=MEMORY, default="8GB")
    screen_size = models.IntegerField()
    cpu = models.CharField(max_length=200, choices=PROCESSOR , default="intel")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering =("Brand",)
       
    
    def __str__(self):
        return '%s %s %s %s'%(self.Brand, self.series, self.memory, self.model)


class Desktop(Computer):
    Brand = models.CharField(max_length=200, choices= BRANDS,default="ASUS")
    series = models.CharField(max_length=200, blank=True)
    model = models.CharField(max_length=200,  default="") 
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    type = models.CharField(max_length=200,choices=DESKTOP_TYPE, default="Desktop type")
    memory = models.CharField(max_length=200, choices=MEMORY, default="8GB")
    screen_size = models.IntegerField()
    cpu = models.CharField(max_length=200, choices=PROCESSOR, default="intel")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) 
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    

    def __str__(self):
        return '%s %s %s %s'%(self.Brand, self.series, self.memory, self.model)


class Review(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)


class OS(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CPU(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Memory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Graphics(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name