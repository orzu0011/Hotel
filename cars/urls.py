from django.urls import path
from cars.views import *


urlpatterns = [
    path("", CarsListAPIView.as_view(), name="list"),
    path("<int:pk>", CarsDetailAPIView.as_view(), name="detail"),
    path("car/", CarListAPIView.as_view(), name="car"),
    path("car/<int:pk>", CarDetailAPIView.as_view(), name="car_detail"),
    path("advantage", CarAdvantagesListAPIView.as_view(), name="advantages"),
    path("advantage/<int:pk>", CarAdvantagesDetailAPIView.as_view(), name="advantages_detail"),    
    path("description", Car_descriptionListAPIView.as_view(), name="about"),
    path("include/", IncludeListAPIView.as_view(), name="include"),
    path("include/<int:pk>", IncludeDetailAPIView.as_view(), name="include_detail"),
    path("description/<int:pk>", Car_descriptionDetailAPIView.as_view(), name="about_detail"),
    path("comment", CommentListAPIView.as_view(), name="comment"),
    path("comment/<int:pk>", CommentDetailAPIView.as_view(), name="comment"),
    path("know", CarInformationListAPIView.as_view(), name="information"),
    path("know/<int:pk>", CarInformationDetailAPIView.as_view(), name="information_detail"),
    path("cost", CarCostListAPIView.as_view(), name="cost"),
    path("cost/<int:pk>", CarCostDetailAPIView.as_view(), name="cost_detail"),
    path("owner", CarOwnerListAPIView.as_view(), name="owner"),
    path("owner/<int:pk>", CarOwnerDetailAPIView.as_view(), name="owner_detail"),
]
