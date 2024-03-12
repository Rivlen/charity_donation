from django.urls import path

from main.views import LandingPageView, DonationPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('donation/', DonationPageView.as_view(), name='donation-page'),
]
