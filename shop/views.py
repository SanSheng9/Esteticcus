from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from .models import Product, Category, PropertyValue, Property
from .serializers import ProductSerializer, CategorySerializer, PropertyValueSerializer, PropertySerializerWithCategory


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [permissions.IsAdminUser]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination

class PropertyValueViewSet(viewsets.ModelViewSet):
    queryset = PropertyValue.objects.all()
    serializer_class = PropertyValueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializerWithCategory
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
