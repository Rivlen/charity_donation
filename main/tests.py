import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_landing_page_200(client):
    url = reverse('landing-page')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_landing_page_dynamic_stats(client, donation):
    url = reverse('landing-page')
    response = client.get(url)

    assertTemplateUsed(response, 'index.html')

    assert response.context['donation_sum'] == 5
    assert response.context['institutions_count'] == 1
    institution = response.context['institution_by_type'][0][0]
    assert institution.name == "Test Institution"
    assert institution.description == "Test"
    assert institution.category.all()[0].name == "Test Category"

