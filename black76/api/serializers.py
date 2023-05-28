from rest_framework import serializers

from .models import Product, Pricing


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'code',
            'name',
            'group',
        ]


class PricingSerializer(serializers.HyperlinkedModelSerializer):
    product_code = serializers.CharField(source='product.code')
    product_name = serializers.CharField(source='product.name')
    product_group = serializers.CharField(source='product.group')

    class Meta:
        model = Pricing
        fields = [
            'id',
            'product_code',
            'product_name',
            'product_group',
            'last',
            'volume',
            'date',
        ]
