import re

from django import forms

from .widgets import BSSearchWidget

PLACEHOLDER = "https://masterbootrecord.bandcamp.com/album/internet-protocol"

class BandcampForm(forms.Form):
    REGEX = """(|https?//:)(.*)\.bandcamp\.com(/album/(.*)|/?)"""
    album_url = forms.URLField(label="", help_text="", widget=BSSearchWidget(
        attrs={'id': 'BandcampForm',
               "class": "form-control",
               "value": PLACEHOLDER,
               "placeholder": PLACEHOLDER,
               }))

    def _match_url(self, in_url: str) -> re.Match:

        match = re.match(self.REGEX, in_url)
        return match

    def is_valid(self) -> bool:
        valid = super().is_valid()

        if not valid:
            return valid

        album_url = self.cleaned_data['album_url']
        match_url = self._match_url(album_url)

        if match_url:
            return True

        return False
