from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from main.models import Category, Institution, Address, Donation


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

        context = {'categories': categories}
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
        return render(request, 'form-confirmation.html')


class GetInstitutionsByCategoriesAPI(View):
    def get(self, request):
        # Get the list of category IDs from the request, removing any slashes
        ids = request.GET.getlist('type_ids')
        ids = [temp_id.replace('/', '') for temp_id in ids]  # Remove any slashes from the ids

        try:
            # Now safely convert to integers
            ids = [int(temp_id) for temp_id in ids]
        except ValueError as e:
            # Handle the case where conversion to integer fails
            return JsonResponse({'error': str(e)}, status=400)

        # The number of categories we're filtering against
        num_categories = len(ids)

        # Filter institutions by those categories and annotate the count of distinct categories
        institutions = Institution.objects \
            .filter(category__id__in=ids) \
            .annotate(num_categories=Count('category', distinct=True)) \
            .filter(num_categories=num_categories)

        # Serialize the institution data
        institutions_data = [{'id': institution.id, 'name': institution.name, 'description': institution.description}
                             for institution in institutions]

        return JsonResponse(institutions_data, safe=False)
