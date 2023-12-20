from rest_framework import serializers

from user.serializer import UserSerializer
from . import models


class FisherySerializer(serializers.ModelSerializer):
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    user_added = UserSerializer(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = models.Fishery
        fields = (
            'name',
            'description',
            'category',
            'latitude',
            'longitude',
            'date_added',
            'user_added',
            'status',
        )


class FisheryLocationFilterSerializer(serializers.Serializer):
    user_lat = serializers.FloatField(required=False)
    user_lon = serializers.FloatField(required=False)
    max_radius = serializers.IntegerField(required=False)

class PictureSerializer(serializers.ModelSerializer):
    user_added = UserSerializer(read_only=True)
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')
    fishery = serializers.StringRelatedField()
    class Meta:
        model = models.Picture
        fields = (
            'title',
            'description',
            'date_added',
            'user_added',
            'fishery',
            'img',
        )