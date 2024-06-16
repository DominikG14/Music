from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Views imports
from django.shortcuts import render, redirect
from utils.views import get_template
from . import urls, forms


def download_song(request: HttpRequest) -> HttpResponse:
    template = get_template(app=urls.app_name)

    if request.method == 'GET':
        form = forms.DownloadSongForm()

    if request.method == 'POST':
        form = forms.DownloadSongForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, template, {
        'form': form,
    })


def download_playlist(request: HttpRequest) -> HttpResponse:
    pass