from django.db import models
from userbase.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)


class Institution(models.Model):
    INSTITUTION_TYPES = {
        1: "Fundacja",
        2: "Organizacja Porządkowa",
        3: "Zbiórka Lokalna",
    }
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=1)
    category = models.ManyToManyField(Category)


class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)


class Donation(models.Model):
    quantity = models.IntegerField()
    category = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
