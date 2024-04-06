from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import MyUser, Coord, Level, Images, Pereval
from .serializers import CoordSerializer, UserSerializer, LevelSerializer, ImagesSerializer, PerevalSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        try:
            user_data = data.get('user')
            coords_data = data.get('coords')
            level_data = data.get('level')
            images_data = data.get('images')

            user_serializer = UserSerializer(data=user_data)
            coords_serializer = CoordSerializer(data=coords_data)
            level_serializer = LevelSerializer(data=level_data)
            images_serializers = [ImagesSerializer(data=image_data) for image_data in images_data]

            if user_serializer.is_valid() and coords_serializer.is_valid() and level_serializer.is_valid() and all(
                    image_serializer.is_valid() for image_serializer in images_serializers):
                user_instance = user_serializer.save()
                coords_instance = coords_serializer.save()
                level_instance = level_serializer.save()

                pereval_data = {
                    'user': user_instance.id,
                    'coords': coords_instance.id,
                    'level': level_instance.id,
                    **data
                }

                pereval_serializer = PerevalSerializer(data=pereval_data)
                if pereval_serializer.is_valid():
                    pereval_instance = pereval_serializer.save()

                    for image_serializer in images_serializers:
                        image_serializer.save(pereval=pereval_instance)

                    return Response({'status': 200, 'message': 'Отправлено успешно', 'id': pereval_instance.id},
                                    status=status.HTTP_200_OK)
            else:
                return Response({'status': 400, 'message': 'Bad Request, недостаточно полей', 'id': None},
                                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'status': 500, 'message': str(e), 'id': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
