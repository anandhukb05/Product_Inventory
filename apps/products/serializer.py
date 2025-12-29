from rest_framework import serializers
from .models import Product


class ProductSerialzer(serializers.ModelSerializer):
    class meta:
        model = Product
        fields= "__all__"

    def validate(self, data):
        name = data.get('name')
        price = data.get('price')
        stock = data.get('stock')

        if not name:
            raise serializers.ValidationError(
                {"name": "Product name is required."}
            )

        if price is not None and price < 0:
            raise serializers.ValidationError(
                {"price": "Price cannot be negative."}
            )

        if stock is not None and stock < 0:
            raise serializers.ValidationError(
                {"stock": "Stock cannot be negative."}
            )

