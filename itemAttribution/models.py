from django.db import models
from baseServer.models import ModelBase


class ProductCategory(ModelBase):
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(ModelBase):
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey("Brand", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductProduct(ModelBase):
    name = models.CharField(max_length=100)
    categ_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

