from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ProductDetailView

router = DefaultRouter()
router.register(r'products', ProductDetailView, basename='task')
urlpatterns = [
    path('', include(router.urls)),
]
