from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, PropertyValueViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'property-values', PropertyValueViewSet)
router.register(r'properties', PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]