from rest_framework.serializers import ModelSerializer
from places.models import Place
from rest_framework import serializers


class PlaceSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "name", "featured_image", "place")
        model = Place


class PlaceDetailsSerializer(ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:
        fields = ("id", "name", "featured_image", "place", "description", "category")
        model = Place

    def get_category(self, instance):
        return instance.category.name