from unittest.mock import MagicMock
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse

from bmbhelper.forms import BandcampForm
from bmbhelper.views import LandingView


class TestLandingView(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('landing')

    def test_status_code_is_for_landing_view(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_landing_view_renders_url_input_form(self):
        response = self.client.get(self.url)
        form = BandcampForm()
        self.assertContains(response, form)

    def test_landing_post_returns_400_for_non_url_string(self):
        response = self.client.post(self.url, {'album_url': 'non url object'})
        self.assertEquals(response.status_code, 400)
        # self.assertFormError(response, 'form', 'album_url', 'This field is required.')

    def test_landing_post_returns_400_for_url_malformed_url_string(self):
        response = self.client.post(self.url, {'album_url': 'https://.com'})
        self.assertEquals(response.status_code, 400)

    def test_landing_post_returns_400_for_non_bandcamp_url(self):
        response = self.client.post(self.url, {'album_url': 'https://google.com'})
        self.assertEquals(response.status_code, 400)

    def test_landing_post_returns_200_for_bandcamp_url(self):
        response = self.client.post(self.url, {'album_url': "https://masterbootrecord.bandcamp.com/album/internet-protocol"})
        self.assertEquals(response.status_code, 200)
