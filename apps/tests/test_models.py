import pytest

from apps.models import Product

@pytest.mark.django_db
def test_product_model():
    product = Product.objects.create(
        name="Test Product",
        price=100,
    )
    assert product.name == "Test Product"
    assert product.price == 100
