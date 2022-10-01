from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Country(ModelBase):
    name = models.CharField(max_length=100)
    idd = models.CharField(max_length=5, blank=True, null=True)
    ccd = models.IntegerField(default=0)
    iso_code = models.CharField( max_length=100, blank=True)

    def __str__(self):
        return self.name



class State(ModelBase):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class City(ModelBase):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name