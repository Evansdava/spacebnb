from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.urls import reverse_lazy
from .models import Listing


class ListingListView(ListView):
    """Renders a list of all listings"""

    model = Listing

    def get(self, request):
        """GET a list of listings"""
        listings = self.get_queryset().all().order_by("start_date")
        return render(request, 'listings/list.html', {'listings': listings})


class ListingDetailView(DetailView):
    """Renders a detailed view of a specific listing based on slug"""

    model = Listing

    def get(self, request, slug):
        """GET the view associated with a slug"""
        listing = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'listings/detail.html', {'listing': listing})


def index(request):
    return HttpResponse("Hello, world. You're at the spacebnb index.")
