from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'index.html'


class DonationPageView(TemplateView):
    template_name = 'form.html'
