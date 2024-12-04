from django import forms
from django.db import models
from pytils.translit import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False, blank=True)


    def __str__(self):
            return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



class ExploreMore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.CharField("URL-фото", max_length=500)

    def __str__(self):
        return self.name



class Tour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tours')
    image = models.CharField("URL-фото", max_length=500)
    
    

    def __str__(self):
        return self.name
        


class CardTour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='card_tour')
    image = models.CharField("URL-фото", max_length=500)
    description = models.TextField("Описание", blank=True, null=True)
    gallery = models.CharField("Галерея изображений", max_length=1000, blank=True, null=True) 
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField(default='2024-01-01') 
    end_date = models.DateField(default='2024-02-01') 

    def get_gallery_images(self):
        return self.gallery.split(',') if self.gallery else []

    def __str__(self):
        return self.name



class Hotel(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, default='Unknown')
    max_guests = models.PositiveIntegerField()  
    rooms_count = models.PositiveIntegerField()
    image = models.CharField("URL-фото", max_length=500)
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField("Описание", blank=True, null=True,)

    def __str__(self):
        return self.name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    gallery = models.CharField("Галерея изображений", max_length=1000, blank=True, null=True)  

    def get_gallery_images(self):

        return self.gallery.split(',') if self.gallery else []

    def __str__(self):
        return f"{self.hotel.name} - Image"






































