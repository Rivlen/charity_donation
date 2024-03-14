import pytest
from main.models import Category, Institution, Address, Donation
from userbase.models import User
import datetime


@pytest.fixture
def category():
    category = Category.objects.create(name="Test Category")
    return category


@pytest.fixture
def institution(category):
    institution = Institution.objects.create(name="Test Institution",
                                             description="Test",
                                             type=1)
    institution.save()
    institution.category.add(category)
    return institution


@pytest.fixture
def address():
    address = Address.objects.create(street_address="Test Street",
                                     city="Test",
                                     postal_code="11-101")
    return address


@pytest.fixture
def user():
    user = User.objects.create_user(username='testuser',
                                    password='password123')
    return user


@pytest.fixture
def donation(category, institution, address, user):
    donation = Donation.objects.create(quantity=5,
                                       phone_number="123456789",
                                       pick_up_date=datetime.date.today(),
                                       pick_up_time=datetime.time(12, 10, 0),
                                       pick_up_comment="Test Comment",
                                       address=address,
                                       institution=institution,
                                       user=user)
    donation.save()
    donation.category.add(category)
    return donation
