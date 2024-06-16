from django import forms
from . import models

from django.conf import settings
from pytube import YouTube


class DownloadSongForm(forms.ModelForm):
    class Meta:
        model = models.Song
        fields = ['yt_url']
    
    def save(self, commit: bool = False) -> models.Song:
        song = super().save(commit=False)

        yt = YouTube(song.yt_url)
        song.title = yt.title

        song.download()
        song.set_metadata()

        if commit:
            song.save()
        
        return song