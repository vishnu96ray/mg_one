from django.db import models
from baseServer.models import ModelBase


# Create your models here.
class StockWarehouse(ModelBase):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name