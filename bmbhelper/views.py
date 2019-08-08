from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import BandcampForm
from .utils.bandcamp_parser import BandcampParser

"""
TemplateResponseMixin \
ContextMixin           - TemplateView
View                  /

if using `TemplateView` & we want to render different templates based on POST & GET
We will need to override the `def get_template_names` from
TemplateResponseMixin class
"""


class LandingView(View):

    def get(self, request, *args, **kwargs):
        form = BandcampForm()
        return render(request, 'bmbhelper/landing.html', {"form": form})

    def post(self, request, parser=BandcampParser, *args, **kwargs):
        form = BandcampForm(request.POST, auto_id=False)
        print(form)

        if not form.is_valid():
            # In really user will be prompted with a toolbox if his entry is not url
            # but for unit tests and overall clarity we will re-render the initial form w/
            # status=400 for initial clarity
            return render(request, 'bmbhelper/landing.html', {"form": form},
                          status=400)

        cd = form.cleaned_data
        album_url = cd.get('album_url')
        form = parser(album_url)
        form.fetch_album()
        form = form.to_dict()
        form["tool_url"] = request.build_absolute_uri(
            reverse('landing'))  # field added for app promotion
        return render(request, 'bmbhelper/results.html', form)


class SandBoxView(View):

    def get(self, request , *args, **kwargs):

        from unittest.mock import MagicMock
        from bs4 import BeautifulSoup

        album_url = "https://masterbootrecord.bandcamp.com/album/internet-protocol"

        from .tests.data.album import album_html

        soup = BeautifulSoup(album_html, "html.parser")
        form = BandcampParser(album_url)
        form.fetch_url_soup = MagicMock(return_value=soup)
        form.fetch_album()

        form = form.to_dict()
        form["tool_url"] = request.build_absolute_uri(
            reverse('landing'))  # field added for app promotion
        return render(request, 'bmbhelper/results.html', form)
