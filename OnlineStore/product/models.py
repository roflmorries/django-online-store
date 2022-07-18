from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=320)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
