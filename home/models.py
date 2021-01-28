from django.db import models

# Create your models here.

class Advert(models.Model):
    link_url = models.URLField(max_length=1024, null=True, blank=True)
    banner = models.ImageField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name