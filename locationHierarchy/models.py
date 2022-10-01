from django.db import models
from baseServer.models import ModelBase
from stockWarehouse.models import StockWarehouse


class LocationHierarchy(ModelBase):
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey("LocationHierarchy", on_delete=models.CASCADE, null=True, blank=True)
    stock_warehouse = models.ForeignKey(StockWarehouse, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name