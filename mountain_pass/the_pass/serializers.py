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
    data = serializers.URLField()
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
                  'user', 'coords', 'level', 'images']

    def create(self, validated_data):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        pass_user = User.objects.filter(email=user['email'])

        if pass_user.exists():
            user_ser = UserSerializer(data=user)
            user = user_ser.save()
        else:
            user = User.objects.create(**user)

        coords = Coord.objects.create(**coords)
        level = Level.objects.create(**level)

        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level)

        for i in images:
            data = i.pop('data')
            title = i.pop('title')
            Images.objects.create(data=data, pereval=pereval, title=title)

        return pereval

