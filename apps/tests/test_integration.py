import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from apps.models import Product
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_product_crud_integration():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    client.login(username="testuser", password="testpass")

    # Create
    create_data = {"name": "Integration Product", "price": 300, "description": "Test"}
    create_response = client.post(reverse("task-list"), create_data, format="json")
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # Read
    read_response = client.get(reverse("task-detail", kwargs={"pk": product_id}))
    assert read_response.status_code == 200
    assert read_response.json()["name"] == "Integration Product"

    # Update
    update_data = {"name": "Updated Product", "price": 350, "description": "Updated"}
    update_response = client.put(reverse("task-detail", kwargs={"pk": product_id}), update_data, format="json")
    assert update_response.status_code == 200
    assert Product.objects.get(id=product_id).name == "Updated Product"

    # Delete
    delete_response = client.delete(reverse("task-detail", kwargs={"pk": product_id}))
    assert delete_response.status_code == 204
    assert Product.objects.count() == 0