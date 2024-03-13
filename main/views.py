from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Donation


class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        donations = Donation.objects.all()
        donation_sum = 0
        institutions = []
        for donation in donations:
            donation_sum += donation.quantity
            institutions.append(donation.institution)
        unique_institutions_amount = len(set(institutions))
        return {'donation_sum': donation_sum, 'unique_institutions_amount': unique_institutions_amount}


class DonationPageView(TemplateView):
    template_name = 'form.html'
