import requests

from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .g2p_utils import prepare_the_checkout

class LandingView(View):

    def get(self, request , *args, **kwargs):
        form = {}
        response = prepare_the_checkout()

        json = response.json()

        checkout_id = json["id"]

        form["checkout_id"] = checkout_id
        form["shopper_result_url"] = "https://risika.dk/"  # TODO: Add to config
         
        return render(request, 'gate2payments/landing.html', {"form": form})


    def post(self, request, *args, **kwargs):
        pass
        # 1. generate custom user id
        # 2. store request info in DB
        # 3. get URL from S2S


class CheckoutCallbackView(View):
    """Listens for callbacks and parses uuid from payment status."""

    def get(self, request , *args, **kwargs):
        form = {}
        response = prepare_the_checkout()

        json = response.json()

        checkout_id = json["id"]

        form["checkout_id"] = checkout_id
        form["shopper_result_url"] = "https://risika.dk/"  # TODO: Add to config
         
        return render(request, 'gate2payments/landing.html', {"form": form})


    def post(self, request, *args, **kwargs):
        pass
        # 1. generate custom user id
        # 2. store request info in DB
        # 3. get URL from S2S