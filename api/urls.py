from django.urls import path
from api.views import *



urlpatterns = [
   path("", CountryListAPIView.as_view(), name="list"),
   path("<int:pk>/", CountryDetailAPIView.as_view(), name="detail"),
   path("authors/", AuthorListAPIView.as_view(), name="author"),
   path("authors/<int:pk>/", AuthorDetailAPIView.as_view(), name="author_detail"),
   path("hotel/", HotelInCityListAPIView.as_view(), name="about"),
   path("hotel/<int:pk>/", HotelInCityDetailAPIView.as_view(), name="about_detail"),
   path("comment/", CommentListAPIView.as_view(), name="comment"),
   path("comment/<int:pk>/", CommentDetailAPIView.as_view(), name="comment_detail"),
   path("information/", InformationListAPIView.as_view(), name="information"),
   path("information/<int:pk>/", InformationDetailAPIView.as_view(), name="information_detail"),
   path("hotelcost/", HotelInCityCostListAPIView.as_view(), name="HotelListAPIView"),
   path("hotelcost/<int:pk>/", HotelInCityCostDetailAPIView.as_view(), name="HotelListAPIView"),
   
]