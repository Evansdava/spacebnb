from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListingListView.as_view(), name='listing-list'),
    path('<str:slug>/', views.ListingDetailView.as_view(),
         name='listing-detail')
]
