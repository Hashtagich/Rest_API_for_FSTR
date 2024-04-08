from rest_framework import status, generics
from rest_framework import viewsets
from django.http import JsonResponse
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
        serializer = PerevalSerializer(data=request.data)

        """Результаты метода: JSON"""
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data,
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad Request',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()

        new_email = request.data.get('user', {}).get('email')
        if new_email:
            existing_user = MyUser.objects.filter(email=new_email).exclude(pk=pereval.user.pk)
            if existing_user.exists():
                return Response({
                    'state': '0',
                    'message': "Пользователь с таким email уже существует."
                })

        serializer = PerevalSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'state': '1',
                'message': 'Запись успешно изменена'
            })
        else:
            return Response({
                'state': '0',
                'message': serializer.errors
            })


class SubmitDataViewSet(viewsets.ViewSet):
    def list(self, request):
        user_email = request.query_params.get('user__email', None)
        if user_email:
            user = MyUser.objects.filter(email=user_email).first()
            if user:
                data_objects = Pereval.objects.filter(user=user)
                serializer = PerevalSerializer(data_objects, many=True)
                return Response(serializer.data)
            else:
                return Response({
                    'message': 'Пользователь с такой почтой не найден',
                    'data': []
                })
        else:
            return Response({
                'message': 'Параметр user__email обязателен',
                'data': []
            })
