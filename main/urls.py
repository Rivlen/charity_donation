from django.urls import path

from main.views import LandingPageView, DonationPageView, DonationConfirmationView, GetInstitutionsByCategoriesAPI

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('donate/', DonationPageView.as_view(), name='donate'),
    path('GetInstitutionsByCategoriesAPI/', GetInstitutionsByCategoriesAPI.as_view(),
         name='get-institutions-by-categories'),
    path('donation-confirmation/', DonationConfirmationView.as_view(), name='donation-confirmation'),
]
