from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from the_pass import views

router = routers.DefaultRouter()
router.register(r'submitData', views.PerevalViewSet, basename='submitData')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]