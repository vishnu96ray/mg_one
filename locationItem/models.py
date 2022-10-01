from django.db import models
from baseServer.models import ModelBase
from itemAttribution.models import ProductProduct
from locationHierarchy.models import LocationHierarchy


class LocationItem(ModelBase):
    name = models.CharField(max_length=100)
    item_id = models.ForeignKey(ProductProduct, on_delete=models.CASCADE, null=True, blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(default=1)
    solo_price = models.FloatField(default=1)
    group_price = models.FloatField(default=1)
    max_quantity = models.IntegerField(default=1)
    is_active = models.BooleanField()
    is_searchable = models.BooleanField(default=False)
    location_hierarchy_id = models.ForeignKey(LocationHierarchy, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name