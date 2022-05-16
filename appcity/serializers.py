from rest_framework import serializers
from .models import *


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'


class ShopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'
