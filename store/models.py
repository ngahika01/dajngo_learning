import email
from django.db import models
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TimeField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
