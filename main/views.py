from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from main.models import Category, Institution, Address, Donation
from django.core import serializers


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
        institutions_count = len(institutions)

        return {'donation_sum': donation_sum, 'institutions_count': institutions_count,
                'institution_by_type': institution_by_type}


class DonationPageView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        categories = Category.objects.all()
        institutions = Institution.objects.all()

        serialized_categories = serializers.serialize('json', categories)
        serialized_institutions = serializers.serialize('json', institutions)

        context = {'categories': categories, 'institutions': institutions,
                   'serialized_categories': serialized_categories, 'serialized_institutions': serialized_institutions}
        return render(request, 'form.html', context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        categories_ids = request.POST.getlist('categories')
        quantity = request.POST.get('bags')
        institution_id = request.POST.get('institution')
        street_address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postcode')
        phone_number = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')

        institution = Institution.objects.get(id=institution_id)
        address_obj = Address(street_address=street_address, city=city, postal_code=postal_code)
        address_obj.save()

        donation = Donation(quantity=quantity, institution=institution, address=address_obj, phone_number=phone_number,
                            pick_up_date=date, pick_up_time=time, pick_up_comment=pick_up_comment, user=request.user)
        donation.save()

        categories = Category.objects.filter(id__in=categories_ids)
        donation.category.add(*categories)
        return redirect('donation-success')


class DonationConfirmationView(TemplateView):
    template_name = 'form-confirmation.html'
