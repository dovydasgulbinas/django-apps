from django.shortcuts import render
from django.urls import reverse
from django.views import View


class LandingView(View):

    def get(self, request , *args, **kwargs):

        form = BandcampParser(album_url)
        form.fetch_url_soup = MagicMock(return_value=soup)
        form.fetch_album()

        form = form.to_dict()
        form["tool_url"] = request.build_absolute_uri(
            reverse('landing'))  # field added for app promotion
        return render(request, 'bmbhelper/results.html', form)