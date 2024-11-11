from rest_framework import serializers
from general_service.models import Picture


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'image')