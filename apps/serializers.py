from rest_framework.serializers import ModelSerializer

from apps.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'id', 'name', 'price'