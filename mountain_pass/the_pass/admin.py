from django.contrib import admin
from .models import Pereval, User, Coord, Level, Images

admin.site.register(User)
admin.site.register(Pereval)
admin.site.register(Coord)
admin.site.register(Level)
admin.site.register(Images)
