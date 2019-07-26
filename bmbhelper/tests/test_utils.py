from unittest.mock import MagicMock

from django.test import TestCase, SimpleTestCase

from bs4 import BeautifulSoup

from bmbhelper.utils.bandcamp_parser import BandcampParser, AlbumMetaData
from .data.album import album_html


class TestBandcampParser(SimpleTestCase):
    URL = "https://masterbootrecord.bandcamp.com/album/internet-protocol"
    ALBUM_HTML = album_html
    N_TRACKS = 7

    def setUp(self):
        self.lw = BandcampParser(self.URL)
        self.soup = BeautifulSoup(self.ALBUM_HTML, "html.parser")
        self.lw.fetch_url_soup = MagicMock(return_value=self.soup)
        self.album_meta = \
            AlbumMetaData("MASTER BOOT RECORD",
                          "INTERNET PROTOCOL",
                          "2019-03-20",
                          "https://f4.bcbits.com/img/a1521867852_16.jpg",
                          "https://masterbootrecord.bandcamp.com/album/internet-protocol"
                          )

    def test_mock_returns_soup_object(self):
        self.assertIsInstance(self.lw.fetch_url_soup(self.URL), BeautifulSoup)

    def test_parse_meta_returns_AlbumMetaData_instance(self):
        self.assertIsInstance(self.lw.parse_meta(self.soup), AlbumMetaData)

    def test_parse_meta_sets_release_meta_attribute(self):
        self.lw.parse_meta(self.soup)
        self.assertIsInstance(self.lw.release_meta, AlbumMetaData)

    def test_parse_meta_parses_fields_correctly(self):
        self.assertEqual(self.lw.parse_meta(self.soup), self.album_meta)

    def test_parse_tracks_is_len_eq_7(self):
        self.lw.parse_tracks(self.soup)
        print(self.lw.release_tracks)
        self.assertEqual(len(self.lw.release_tracks), self.N_TRACKS)

    def test_fetch_album_sets_class_variables(self):
        self.lw.fetch_album()
        self.assertEqual(self.lw.parse_meta(self.soup), self.album_meta)
        self.assertIsInstance(self.lw.release_meta, AlbumMetaData)
