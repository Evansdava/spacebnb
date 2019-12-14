from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from listings.models import Listing
from api.serializers import ListingSerializer


class ListingList(APIView):
    def get(self, request):
        listings = Listing.objects.all()[:20]
        data = ListingSerializer(listings, many=True).data
        return Response(data)


class ListingDetail(APIView):
    def get(self, request, slug):
        listing = get_object_or_404(Listing, slug=slug)
        data = ListingSerializer(listing).data
        return Response(data)
