from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
        )

    def ___str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    class MPTTMeta:
        order_insertion_by = ['name']

    def ___str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        'Category', null=True, on_delete=models.SET_NULL, blank=True
    )

    def ___str__(self):
        return self.name
