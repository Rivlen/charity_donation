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
    assert response.context['unique_institutions_amount'] == 1
