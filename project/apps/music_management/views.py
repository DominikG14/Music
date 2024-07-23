from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Music imports
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

# Views imports
from django.shortcuts import render, redirect
from utils.views import get_template
from . import urls, forms


def download_song(request: HttpRequest) -> HttpResponse:
    def load_yt(yt_url: str) -> YouTube:
        """Loads YouTube video and checks for accessibility"""
        try:
            yt = YouTube(yt_url)
            yt.check_availability() # raises exceptions
        
        # TODO: Check for variety of exceptions
        except VideoUnavailable:
            pass

        return yt

    template = get_template(app=urls.app_name)
    context = {'download': False}

    if request.method == 'GET':
        form = forms.DownloadSongForm()

    if request.method == 'POST':
        form = forms.DownloadSongForm(request.POST)

        if form.is_valid():
            form.save()
        
        if yt_url := form.cleaned_data.get('yt_url'):
            yt = load_yt(yt_url)
            
            context.update({
                'download': True,
                'cover_url': yt.thumbnail_url,          
            })
            form = forms.DownloadSongForm({
                'yt_url': yt_url,
                'title': yt.title,
                'download': True,
                'save_to_library': True,
            })

    print(request.POST)
    context.update({'form': form})
    return render(request, template, context)


def download_playlist(request: HttpRequest) -> HttpResponse:
    pass