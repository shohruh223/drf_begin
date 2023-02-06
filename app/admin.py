from django.contrib import admin

from app.models import Product, Comment, Category

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Category)