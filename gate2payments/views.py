from django.shortcuts import render
from django.urls import reverse
from django.views import View
import requests


class LandingView(View):

    def get(self, request , *args, **kwargs):
        form = {}


        url = "https://test.oppwa.com/v1/checkouts"
        params = {
            'entityId' : '8a8294174ed9c2b5014ede67e92406ef',
            'amount' : 92.00,
            'currency' : 'EUR',
            'paymentType' : 'DB',
            'createRegistration' : True
        }

        headers = {"Authorization": "Bearer OGE4Mjk0MTc0ZWQ5YzJiNTAxNGVkZTY3ZTkzMjA2ZjN8SjR5SnhUYkNncw=="}

        r = requests.get(url, params=params, headers=headers)
        print(r._content_consumed)
        print(r.content)
        # print(r.json())
        print("REEEEE")

        form["tool_url"] = request.build_absolute_uri(reverse('landing'))  # field added for app promotion
        return render(request, 'gate2payments/landing.html', form)


    def post(self, request, *args, **kwargs):
        pass
        # 1. generate custom user id
        # 2. store request info in DB
        # 3. get URL from S2S
