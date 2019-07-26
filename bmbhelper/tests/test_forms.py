import re
import types
from unittest.mock import MagicMock
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from bmbhelper.forms import BandcampForm


class TestBandcampForm(SimpleTestCase):

    URL_GOOD_BASE = "https://masterbootrecord.bandcamp.com"
    URL_GOOD = "https://masterbootrecord.bandcamp.com/album/internet-protocol"
    URL_BAD_GENERIC = "example.com"

    def setUp(self):
        self.bf = BandcampForm()

    def test_match_url_returns_re_Match_type(self):
        match = self.bf._match_url(self.URL_GOOD)
        self.assertIsInstance(match, re.Match)

    def test_match_url_returns_Nonetype_w_bad_url(self):
        match = self.bf._match_url(self.URL_BAD_GENERIC)
        self.assertIsNone(match)

    def test_match_url_return_false_on_exmaplecom(self):
        match = self.bf._match_url(self.URL_BAD_GENERIC)
        self.assertFalse(match)

    def test_match_url_returns_true_on_album_url(self):
        match = self.bf._match_url(self.URL_GOOD)
        self.assertTrue(match)

    def test_form_is_valid_returns_false_w_non_bandcamp(self):
        self.bf.album_url = self.URL_BAD_GENERIC
        is_valid = self.bf.is_valid()
        self.assertFalse(is_valid, f'{is_valid} {self.bf.album_url} does not match {self.bf.REGEX}')

    def test_match_url_returns_true_with_base_url(self):
        match = self.bf._match_url(self.URL_GOOD_BASE)
        self.assertTrue(match)
