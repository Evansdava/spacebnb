from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Listing, ListingForm


class ListingListView(ListView):
    """Renders a list of all listings"""

    model = Listing

    def get(self, request):
        """GET a list of listings"""
        listings = self.get_queryset().all().order_by("start_date")
        username = None
        auth = request.user.is_authenticated
        if auth:
            username = request.user.username
        return render(request, 'listings/list.html', {'listings': listings,
                                                      'username': username,
                                                      'auth': auth})


class ListingDetailView(DetailView):
    """Renders a detailed view of a specific listing based on slug"""

    model = Listing

    def get(self, request, slug):
        """GET the view associated with a slug"""
        listing = self.get_queryset().get(slug__iexact=slug)
        username = None
        auth = request.user.is_authenticated
        if auth:
            username = request.user.username
        return render(request, 'listings/detail.html', {'listing': listing,
                                                        'username': username,
                                                        'auth': auth})

    def post(self, request, slug):
        """POST the button to assign a listing to a user"""
        auth = request.user.is_authenticated
        user = None
        username = None
        if auth:
            user = request.user
            username = user.username
        listing = self.get_queryset().get(slug__iexact=slug)
        listing.guest.set([user])
        listing.save()
        return render(request, 'listings/detail.html', {'listing': listing,
                                                        'username': username,
                                                        'auth': auth})


class BookedListView(ListView):
    """Show the user's booked listings"""
    model = Listing

    def get(self, request):
        """GET the list of booked listings for the user"""
        username = None
        user = None
        auth = request.user.is_authenticated
        if auth:
            user = request.user
            username = request.user.username
        listings = self.get_queryset().filter(guest=user)\
            .order_by("start_date")

        return render(request, 'listings/booked.html', {'listings': listings,
                                                        'username': username,
                                                        'auth': auth})


class NewListingView(CreateView):
    """Returns a form for a new listing"""

    template_name = 'listings/new_listing.html'
    form_class = ListingForm
    success_url = reverse_lazy('listing-list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
