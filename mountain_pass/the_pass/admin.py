from django.contrib import admin
from .models import Pereval, MyUser, Coord, Level, Images

admin.site.register(MyUser)
admin.site.register(Pereval)
admin.site.register(Coord)
admin.site.register(Level)
admin.site.register(Images)
