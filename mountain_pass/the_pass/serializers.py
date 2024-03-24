from .models import Coord, Level, Pereval, Images, MyUser
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
        model = MyUser
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
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')

        pass_user = MyUser.objects.filter(email=user_data['email'])

        if pass_user.exists():
            user_ser = UserSerializer(data=user_data)
            user = user_ser.save()
        else:
            user = MyUser.objects.create(**user_data)

        coords = Coord.objects.create(**coords_data)
        level = Level.objects.create(**level_data)

        pereval = Pereval.objects.create(user=user, coords=coords, level=level, **validated_data)

        for i in images_data:
            data = i.pop('data')
            title = i.pop('title')
            Images.objects.create(data=data, pereval=pereval, title=title)

        return pereval
