from django.urls import path

from api.views import ListingList, ListingDetail

urlpatterns = [
    path('listing/', ListingList.as_view(), name='listing_list'),
    path('listing/<str:slug>', ListingDetail.as_view(), name='listing_detail')
]
