from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=225)
    parent = models.OneToOneField('self',  on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=1000);
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Property(models.Model):
    owner = models.ForeignKey(User, related_name="properties", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,  related_name="properties")
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class PropertyValue(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    owner = models.ForeignKey(Product, related_name='property_values', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.property}: {self.value} ({self.owner})'
