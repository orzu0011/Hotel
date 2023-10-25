from _decimal import Decimal
from api.serializers import *
from country.models import *
from rest_framework.views import APIView, Response
from rest_framework.generics import *
from rest_framework.permissions import *
# from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import *
from rest_framework import filters
from api.serializers import *

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
