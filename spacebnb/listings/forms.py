from django import forms
from listings.models import Listing


class ListingForm(forms.ModelForm):
    """ Render and process a form based on the Listing model. """
    model = Listing
