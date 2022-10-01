from rest_framework import serializers
from .models import *

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')
        