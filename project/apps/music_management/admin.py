from django.contrib import admin
from . import models


admin.site.register(models.Creator)
admin.site.register(models.Song)
admin.site.register(models.Playlist)