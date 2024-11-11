from django.contrib import admin

from shop.models import Product, Category, Property, PropertyValue

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(PropertyValue)