import re

from django import forms


class BandcampForm(forms.Form):
    REGEX = """(|https?//:)(.*)\.bandcamp\.com(/album/(.*)|/?)"""
    # https://github.com/django/django/tree/master/django/forms/templates/django/forms/widgets
    album_url = forms.URLField()

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
