# wiki/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from listings.models import Listing


class AccountsAppTests(TestCase):
    def test_user_creation(self):
        # Make some test data to be displayed on the Listing.
        user = User.objects.create(username="TestUser")
        queryset = User.objects.get(id=1)
        self.assertEqual(queryset, user)

    def test_user_booking_relation(self):
        user = User.objects.create(username="TestUser")

        listing = Listing.objects.create(name="Test", description="test", owner="Test", price=1.00)

        listing.guest.set([user])
        listing.save()

        self.assertIn(listing, Listing.objects.filter(guest=user))


