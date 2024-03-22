from .models import Coord, Level, Pereval, Images, User
from rest_framework import serializers


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['data', 'title']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']


class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time',
                  'user', 'coords', 'level', 'images', 'status']

    def create(self, validated_data):
        images_data = validated_data.pop('data')
        perevel = Pereval.objects.create(**validated_data)
        for image_data in images_data:
            Images.objects.create(perevel=perevel, **image_data)
        return perevel
