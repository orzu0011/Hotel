from _decimal import Decimal
from django.shortcuts import render
from api.serializers import *
from country.models import *
from rest_framework.views import APIView, Response
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.decorators import action
# from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import *
from rest_framework import filters


class CountryListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["city_name", "properties"]
    search_fields = ["city_name", "properties"]
    
    # def create(self, request, *args, **kwargs):
    #     serializer = CountrySerializer(data=request.POST)
    #     print(serializer.is_valid())
    #     print(serializer.errors)
    #     return super().create(request, *args, **kwargs)


class CountryDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["city_name", "properties"]
    search_fields = ["is", "city_name", "properties"]


class HotelInCityListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = HotelInCity.objects.all()
    serializer_class = HotelInCitySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["id", "city","title"]
    search_fields = ["id", "city","title"]


class HotelInCityDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ # TODO
        IsAuthenticatedOrReadOnly,
    ]
    queryset = HotelInCity.objects.all()
    serializer_class = HotelInCitySerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["id", "city","title"]


class AuthorListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["id", "full_name", "response_time"]
    search_fields = ["id", "full_name", "response_time"]


class AuthorDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["id", "full_name", "response_time"]


class CommentListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["id", "post", "name", "created"]
    search_fields = ["id", "post", "name", "created"]


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["id", "post", "name", "created"]


class InformationListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["id", "hotel", "title"]
    search_fields = ["city_name", "properties"]


class InformationDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["id", "hotel", "title"]

class HotelInCityCostListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,  
    ]
    queryset = HotelInCityCost.objects.all()
    serializer_class = HotelInCityCostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filter_fields = ["id", "room_price_per_day", "room_check_in", "room_check_out", "day"]
    search_fields = ["id", "room_price_per_day", "room_check_in", "room_check_out", "day"]


class HotelInCityCostDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = HotelInCityCost.objects.all()
    serializer_class = HotelInCityCostSerializer
    search_fields = ["id", "room_price_per_day", "room_check_in", "room_check_out", "day"]
