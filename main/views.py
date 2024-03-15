from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import Donation, Institution


class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        donations = Donation.objects.all()
        donation_sum = 0
        for donation in donations:
            donation_sum += donation.quantity

        institutions = Institution.objects.all()
        institution_by_type = []
        for i in range(1, 4):
            institution_by_type.append(list(institutions.filter(type=i)))
        unique_institutions_count = len(institutions)

        return {'donation_sum': donation_sum, 'unique_institutions_count': unique_institutions_count,
                'institution_by_type': institution_by_type}


class DonationPageView(TemplateView):
    template_name = 'form.html'
