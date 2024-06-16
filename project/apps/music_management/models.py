from django.db import models
from django.utils.timezone import now

from django.conf import settings

from pytube import YouTube, Playlist
from mutagen.mp4 import MP4, MP4Cover
import requests


class Creator(models.Model):
    yt_url = models.URLField()
    name = models.CharField(max_length=255)

    create_date = models.DateTimeField(default=now)
    alter_date = models.DateField(default=now)


class Song(models.Model):
    # urls
    yt_url = models.URLField()

    # song info
    title = models.CharField(max_length=255)
    creators = models.ManyToManyField(Creator)

    # file info
    length = models.IntegerField(blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)

    # date info
    create_date = models.DateTimeField(default=now)
    alter_date = models.DateField(default=now)


    def get_mp4_url(self) -> str:
        return f'{settings.MEDIA_ROOT}/songs/{self.title}.mp4'
    

    def get_cover_url(self) -> str:
        yt = YouTube(self.yt_url)
        return yt.thumbnail_url


    def download(self) -> None:
        FORBIDDEN_CHARACTERS = ['*', '"', '/', '\\', '<', '>', ':', '|', '?']

        yt = YouTube(self.yt_url)
        
        yt.streams.filter(only_audio=True, file_extension='mp4') \
                .first() \
                .download(filename=self.get_mp4_url())
    

    def set_metadata(self) -> None:
        TITLE = '\xa9nam'
        ARTIST = '\xa9ART'
        ALBUM = '\xa9alb'
        COVER = 'covr'
        
        mp4 = MP4(self.get_mp4_url())
        mp4[TITLE] = self.title
        # mp4[ARTIST] = TODO: Loop through avery artist and add here 
        cover = requests.get(self.get_cover_url()).content
        mp4[COVER] = [MP4Cover(cover, imageformat=MP4Cover.FORMAT_JPEG)]
        mp4.save()


    def __str__(self) -> str:
        return self.title


class Playlist(models.Model):
    create_date = models.DateTimeField(default=now)
    alter_date = models.DateField(default=now)

    name = models.CharField(max_length=255)    
    songs = models.ManyToManyField(Song)