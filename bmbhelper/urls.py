from django.urls import path

from . views import LandingView, SandBoxView

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('sandbox', SandBoxView.as_view(), name='sandbox'),

]