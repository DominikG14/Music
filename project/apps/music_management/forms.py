from django import forms
from . import models

from utils.forms import FormSetup

from pytube import YouTube


class DownloadSongForm(forms.ModelForm):
    download = forms.BooleanField(required=False)
    save_to_library = forms.BooleanField(required=False)


    class Meta:
        model = models.Song
        fields = [
            'yt_url',
            'title',
            'download',
            'save_to_library'
        ]

        widgets = {
            'yt_url': forms.URLInput(attrs={'placeholder': 'YouTube song url'})
        }
    
    
    def save(self, commit: bool = False) -> models.Song:
        song = super().save(commit=False)
        save_to_library = self.cleaned_data.get('save_to_library')
        download = self.cleaned_data.get('download')

        yt = YouTube(song.yt_url)
        song.title = yt.title
        song.cover_url = yt.thumbnail_url

        if download:
            song.download()
            song.set_metadata()

        if commit and save_to_library:
            song.save()
        
        return song