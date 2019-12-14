from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.text import slugify


# Create your models here.
class Listing(models.Model):
    """Model for listings, including name, price, location, features, etc."""

    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=17, decimal_places=2)
    description = models.CharField(max_length=200, default="")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    location = models.CharField(max_length=50)
    owner = models.CharField(max_length=20)
    img_url = models.URLField(default="https://via.placeholder.com/300")
    slug = models.SlugField(max_length=100, blank=True, null=True)
    guest = models.ManyToManyField(User)

    def __str__(self):
        """Display the name of the listing when asked for a string"""
        return self.name

    def save(self, *args, **kwargs):
        """Creates a URL safe slug when a new a listing is created."""
        if not self.pk:
            self.slug = slugify(self.name, allow_unicode=True)

        # Call save on the superclass.
        return super(Listing, self).save(*args, **kwargs)


class ListingForm(ModelForm):
    """Form for new listings"""

    class Meta:
        model = Listing
        fields = ['name', 'owner', 'description', 'price', 'start_date',
                  'end_date', 'location', 'img_url']
