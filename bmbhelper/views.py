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




