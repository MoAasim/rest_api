
from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    serial_number = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['serial_number', 'name', 'description', 'price']
    
    def get_serial_number(self, obj):
        return obj.pk