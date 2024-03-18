from .models import Coord, Level, Pereval, Images, User
from rest_framework import serializers


class CoordSerializer(serializers.HyperlinkedModelSerializer):
    pass


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    pass


class PerevalSerializer(serializers.HyperlinkedModelSerializer):
    pass


class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    pass


class UserSerializer(serializers.HyperlinkedModelSerializer):
    pass

