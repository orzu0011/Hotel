from django.urls import path
from api_view.views import *

urlpatterns = [
    path("hotelcost/", HotelInCityCostListAPIView.as_view(), name="HotelListAPIView"),
    path("hotelcost/<int:pk>/", HotelInCityCostDetailAPIView.as_view(), name="HotelListAPIView"),
]











