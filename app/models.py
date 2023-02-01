from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

