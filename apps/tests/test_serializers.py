import pytest

from apps.serializers import ProductSerializer
from apps.models import Product


@pytest.mark.django_db
def test_product_serializer():
    product = Product.objects.create(
        name="Test Product",
        price=100,
    )
    serializer = ProductSerializer(product)
    data = serializer.data
    assert data["name"] == "Test Product"
    assert float(data["price"]) == 100
