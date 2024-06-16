from django.urls import path
from . import views, redirects


app_name = 'music_management'
urlpatterns = []


PATHS = [
    path('download-song/', views.download_song, name='download_song'),
]

REDIRECTS = [
]


urlpatterns += PATHS
urlpatterns += REDIRECTS