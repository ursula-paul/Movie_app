
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

# class User(models.Model):
#     first_name =models.CharField(max_length = 30)
#     last_name = models.CharField(max_length =30)
#     email = models.CharField(max_length=15)
#     password = models.IntegerField(max_length =25)
    
#     def __str__(self):
#         return self.first_name