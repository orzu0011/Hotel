from _decimal import Decimal
from django.shortcuts import render
from cars.serializers import *
from cars.models import *
from rest_framework.views import APIView, Response
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.decorators import action
# from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import *
from rest_framework import filters


class CarsListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["cars_name", "seats", "choice", "price_days"]
    search_fields = ["cars_name", "seats", "choice", "price_days"]
    
    
class CarsDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["is", "city_name", "properties"]    


class CarListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["name", "car_owner","bags"]
    search_fields = ["name", "car_owner", "bags"]
        

class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["name", "car_owner", "bags"]
    

class CarAdvantagesListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarAdvantages.objects.all()
    serializer_class = CarAdvantagesSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["fuel_consumption", "electric_combined", "touchscreen_display", "light", "forward_collision", "fire", "stop_and_go", "b_c_w"]
    search_fields = ["fuel_consumption", "electric_combined", "touchscreen_display", "light", "forward_collision", "fire", "stop_and_go", "b_c_w"]


class CarAdvantagesDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarAdvantages.objects.all()
    serializer_class = CarAdvantagesSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["fuel_consumption", "electric_combined", "touchscreen_display", "light", "forward_collision", "fire", "stop_and_go", "b_c_w"]


class Car_descriptionListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Car_description.objects.all()
    serializer_class = Car_descriptionSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["description"]
    search_fields = ["description"]
    

class Car_descriptionDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Car_description.objects.all()
    serializer_class = Car_descriptionSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["description"]
    

class IncludeListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Include.objects.all()
    serializer_class = IncludeSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["sentence1", "sentence2", "sentence3", "sentence4", "sentence5", "sentence6"]
    search_fields = ["sentence1", "sentence2", "sentence3", "sentence4", "sentence5", "sentence6"]


class IncludeDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Include.objects.all()
    serializer_class = IncludeSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["sentence1", "sentence2", "sentence3", "sentence4", "sentence5", "sentence6"]


class CarOwnerListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["full_name", "places", "description", "joined", "response", "response_time"]
    search_fields = ["full_name", "places", "description", "joined", "response", "response_time"]


class CarOwnerDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarOwner.objects.all()
    serializer_class = CarOwnerSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["full_name", "places", "description", "joined", "response", "response_time"]


class CommentListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["post", "name", "description", "created"]
    search_fields = ["post", "name", "description", "created"]
    
    
class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["post", "name", "description", "created"]
    
    
class CarInformationListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarInformation.objects.all()
    serializer_class = CarInformationSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["title", "cancellation_policy_title", "cancellation_policy_description", "special_note_title","special_note_description"]
    search_fields = ["title", "cancellation_policy_title", "cancellation_policy_description", "special_note_title","special_note_description"]


class CarInformationDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarInformation.objects.all()
    serializer_class = CarInformationSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["title", "cancellation_policy_title", "cancellation_policy_description", "special_note_title","special_note_description"]


class CarCostListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarCost.objects.all()
    serializer_class = CarCostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filter_fields = ["id", "day", "car_pick_up", "car_drop_off", "car_price_per_day","total_cost","discount"]
    search_fields = ["id", "day", "car_pick_up", "car_drop_off", "car_price_per_day","total_cost","discount"]


class CarCostDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = CarCost.objects.all()
    serializer_class = CarCostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["id", "day", "car_pick_up", "car_drop_off", "car_price_per_day","total_cost","discount"]
