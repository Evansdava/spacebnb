# wiki/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from listings.models import Listing


class ListingListViewTests(TestCase):
    def test_multiple_Listings(self):
        # Make some test data to be displayed on the Listing.
        user = User.objects.create()

        Listing.objects.create(name="My Test Listing", description="test",
                               owner=user, price=2.00)
        Listing.objects.create(name="Another Test Listing", description="test",
                               owner=user, price=2.00)

        # Issue a GET request to the MakeWiki homeListing.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of Listings passed to the template
        # matches the number of Listings we have in the database.
        responses = response.context['listings']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Listing: My Test Listing>', '<Listing: Another Test Listing>'],
            ordered=False
        )


class ListingDetailViewTests(TestCase):
    def test_single_Listing(self):
        # Create a test Listing
        user = User.objects.create()

        listing = Listing(name="Test Listing", description="Test", owner=user, price=2.00)
        listing.save()

        response = self.client.get(reverse('listing-detail',
                                   args=[listing.slug]))

        self.assertEqual(response.status_code, 200)

