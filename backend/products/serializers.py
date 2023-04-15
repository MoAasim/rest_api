from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    #serial_number = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    # def get_serial_number(self, obj):
    #     if hasattr(obj, 'pk'):
    #         return obj.pk
    #     else:
    #         return None