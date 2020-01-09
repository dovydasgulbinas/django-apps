import requests

from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .g2p_utils import prepare_the_checkout


def extract_user_info():
    # GO2ORACLE: steal session ID cookie
    # Resolve user id, amount
    # Return values
    pass


class LandingView(View):

    def get(self, request , *args, **kwargs):
        # AFTER hit to callback FLAG id as used! @DB
        # PRINT USER THAT WE HAVE REGISTERED HIS PAYMENT
        
        form = {}
        response = prepare_the_checkout()

        json = response.json()

        checkout_id = json["id"]

        form["checkout_id"] = checkout_id
        form["shopper_result_url"] = "https://risika.dk/"  # TODO: Add to config
         
        return render(request, 'gate2payments/landing.html', {"form": form})

        form["script"] = """<script src="https://test.oppwa.com/v1/paymentWidgets.js?checkoutId=235B1D5B2C2882C38378C1E5C431514B.uat01-vm-tx03"></script>"""
        form["url"] = "https://test.oppwa.com/v1/paymentWidgets.js?checkoutId=235B1D5B2C2882C38378C1E5C431514B.uat01-vm-tx03"
        # https://dovydas.xyz/?id=235B1D5B2C2882C38378C1E5C431514B.uat01-vm-tx03&resourcePath=%2Fv1%2Fcheckouts%2F235B1D5B2C2882C38378C1E5C431514B.uat01-vm-tx03%2Fpayment
        #?id=235B1D5B2C2882C38378C1E5C431514B.uat01-vm-tx03&resourcePath=/v1/checkouts/235B1D5B2C2882C38378C1E5C431514B.uat01-vm-tx03/payment
        

    def post(self, request, *args, **kwargs):
        pass
        # 1. generate custom user id
        # 2. store request info in DB
        # 3. get URL from S2S

class PromotionView(View):

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