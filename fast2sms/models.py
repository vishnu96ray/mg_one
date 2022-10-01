from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField(null=True, default=0.0)
    date = models.DateTimeField(null=True, auto_now_add=True)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=500, null=True, blank=True)
    otp=models.CharField(max_length=10, null=True, blank=True)
    count=models.IntegerField(default=0)
    
