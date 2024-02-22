from django.db import models


class Product(models.Model):
    vape = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    skew = models.CharField(max_length=100)

    def __str__(self):
        return self.vape


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title
