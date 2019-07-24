from django.urls import path

from . views import LandingView, index

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    # path('', index, name='index'),
]