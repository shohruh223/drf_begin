from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155)


class Product(models.Model):
    title = models.CharField(max_length=155)
    text = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='product/', null=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey('auth.User', models.SET_NULL, null=True, blank=True)
    description = models.TextField()

