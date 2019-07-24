import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.views.generic.base import TemplateView

from bs4 import BeautifulSoup
from typing import Tuple, List

from .forms import BandcampForm

"""
TemplateResponseMixin \
ContextMixin           - TemplateView
View                  /

if using `TemplateView` & we want to render different templates based on POST & GET
We will need to override the `def get_template_names` from
TemplateResponseMixin class
"""


def index(request):
    context = {
        'days': [1, 2, 3],
    }
    return render(request, 'bmbhelper/landing.html', context)


class LandingView(View):

    def get(self, request, *args, **kwargs):
        form = BandcampForm()
        return render(request, 'bmbhelper/landing.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = BandcampForm(request.POST)

        print(form)
        print(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            album_url = cd.get('album_url')

        print(album_url)

        all_data = self._scrape_bandcamp(album_url)
        all_data["album_url"] = album_url

        return render(request, 'bmbhelper/results.html', all_data)

    def _scrape_bandcamp(self, album_url) -> dict:
        soup = self._fetch_url_soup(album_url)
        meta = self._parse_meta(soup)

        return meta

    def _fetch_url_soup(self, album_url):
        r = requests.get(album_url)
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup

    def _parse_meta(self, soup: BeautifulSoup):

        artist = soup.find(itemprop="byArtist").a.text
        album = soup.find(class_="trackTitle").text.strip('\n ')

        release_date = soup.find(itemprop="datePublished")['content']
        # split to YYYY-MM-DD
        release_date = f'{release_date[:4]}-{release_date[4:6]}-{release_date[6:8]}'
        cover_art = soup.find(class_="popupImage").img['src']

        return {
            "artist": artist,
            "album": album,
            "release_date": release_date,
            "cover_art": cover_art,
        }



    def _parse_tracks(self, soup: BeautifulSoup):
        pass


class XLandingView(TemplateView):
    template_name = 'bmbhelper/landing.html'

    # def get(self, request, *args, **kwargs):
    #     context = dict()
    #     return render(request, 'bmbhelper/landing.html', context)
