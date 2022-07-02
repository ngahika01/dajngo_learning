from pyexpat import model
from django.db import models


class Product():
    title = models.CharField(max_length=255)
    description = models.TimeField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    
