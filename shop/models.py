from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=30)
    price = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to='product_images/')

    def display_price(self):
        return str(self.price) + '$'

    def __str__(self):
        return self.name

