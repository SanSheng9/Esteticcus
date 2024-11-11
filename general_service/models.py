from django.db import models

from shop.models import Product


def user_directory_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.id, filename)

class Picture(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
    owner = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)

