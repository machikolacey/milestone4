from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.contrib.auth.models import User



class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.user.username +'/ '+ self.product.name + '/ ' + self.updated_at

class Event(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE
    )    
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    event_title = models.TextField(max_length=250, null=True, blank=True)
    is_virtual = models.BooleanField(default=False, null=True, blank=True)
    video_link = models.TextField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return self.event_title+'/ '+ self.end_date_time.strftime("%m/%d/%Y, %H:%M:%S") 
    

class Album(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete = models.CASCADE
    )
    album_runtime = models.IntegerField(null=False, blank=False)
    album_jacket =  models.ImageField(null=True, blank=True)
