from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.models import Product
from apps.serializers import ProductSerializer


@extend_schema(tags=["Product"])
class ProductDetailView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
