from django.urls import path

from main.views import LandingPageView, DonationPageView, DonationConfirmationView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('donate/', DonationPageView.as_view(), name='donate'),
    path('donation-confirmation/', DonationConfirmationView.as_view(), name='donation-success'),
]
