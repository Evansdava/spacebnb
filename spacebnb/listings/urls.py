from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListingListView.as_view(), name='listing-list'),
    path('booked/', views.BookedListView.as_view(), name='booked-list'),
    path('new/', views.NewListingView.as_view(), name='new-listing'),
    path('<str:slug>/', views.ListingDetailView.as_view(),
         name='listing-detail')
]
