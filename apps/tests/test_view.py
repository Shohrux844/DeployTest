import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.models import Product
from decimal import Decimal


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_list_products(client):
    Product.objects.create(name="Test Product1", price=100)
    Product.objects.create(name="Test Product2", price=200)

    url = reverse("task-list")
    response = client.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["count"] == 2

    names = {item["name"] for item in data["results"]}
    assert names == {"Test Product1", "Test Product2"}


@pytest.mark.django_db
def test_retrieve_product(client):
    prod = Product.objects.create(name="Single", price=300)

    url = reverse("task-detail", args=[prod.pk])
    response = client.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Single"
    assert Decimal(data["price"]) == Decimal("300.00")


@pytest.mark.django_db
def test_create_product(client):
    url = reverse("task-list")
    payload = {"name": "New", "price": "50.00"}
    response = client.post(url, payload, format="json")

    assert response.status_code == 201
    prod = Product.objects.get()
    assert prod.name == "New"
    assert prod.price == Decimal("50.00")


@pytest.mark.django_db
def test_update_product(client):
    prod = Product.objects.create(name="Old", price=5)

    url = reverse("task-detail", args=[prod.pk])
    payload = {"name": "Updated", "price": "15.00"}
    response = client.put(url, payload, format="json")

    assert response.status_code == 200
    prod.refresh_from_db()
    assert prod.name == "Updated"
    assert prod.price == Decimal("15.00")


@pytest.mark.django_db
def test_delete_product(client):
    prod = Product.objects.create(name="ToDelete", price=1)

    url = reverse("task-detail", args=[prod.pk])
    response = client.delete(url)
    assert response.status_code == 204

    # confirm no object remains
    exists = Product.objects.filter(pk=prod.pk).exists()
    assert not exists
