from rest_framework.routers import DefaultRouter

from apps.views import ProductDetailView

router = DefaultRouter()
router.register('', ProductDetailView, basename='task')
urlpatterns = [
              ] + router.urls
