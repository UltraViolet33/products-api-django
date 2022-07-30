from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self) -> str:
        return self.name
