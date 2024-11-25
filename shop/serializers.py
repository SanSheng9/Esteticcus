from rest_framework import serializers

from general_service.serializers import PictureSerializer
from .models import Category, Product, PropertyValue, Property


class PropertyValueSerializer(serializers.ModelSerializer):
    property = serializers.StringRelatedField()

    class Meta:
        model = PropertyValue
        fields = ('id', 'property', 'value')


class ProductSerializer(serializers.ModelSerializer):
    images = PictureSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()
    property_values = PropertyValueSerializer(many=True)

    def create(self, validated_data):
        property_values_data = validated_data.pop('property_values')
        product = Product.objects.create(**validated_data)
        for property_value_data in property_values_data:
            PropertyValue.objects.create(owner=product, **property_value_data)
        return product

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category', 'owner', 'images', 'property_values')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'name')


class PropertySerializerWithCategory(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Property
        fields = ('id', 'name', 'category', 'owner')


class CategorySerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'owner', 'properties')
