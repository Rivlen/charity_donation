from django.urls import path

from main.views import LandingPageView, DonationPageView, GetInstitutionsByCategoriesAPI

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('donate/', DonationPageView.as_view(), name='donate'),
    path('GetInstitutionsByCategoriesAPI/', GetInstitutionsByCategoriesAPI.as_view(),
         name='get-institutions-by-categories'),
]
