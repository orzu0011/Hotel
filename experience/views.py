from _decimal import Decimal
from django.shortcuts import render
from experience.serializers import *
from experience.models import *
from rest_framework.views import APIView, Response
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.decorators import action
# from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import *
from rest_framework import filters



class ExperiencesListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Experiences.objects.all()
    serializer_class = ExperiencesSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["title", "author", "hour", "number_of_people", "language"]
    search_fields = ["title", "author", "hour", "number_of_people", "language"]


class ExperiencesDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Experiences.objects.all()
    serializer_class = ExperiencesSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["title", "author", "hour", "number_of_people", "language"]




class ExperiencesCostListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = ExperiencesCost.objects.all()
    serializer_class = ExperiencesCostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["person_price_per_day", "guests"]
    search_fields = ["person_price_per_day", "guests"]


class ExperiencesCostDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = ExperiencesCost.objects.all()
    serializer_class = ExperiencesCostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["person_price_per_day", "guests"]



class IncludeListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Include.objects.all()
    serializer_class = IncludeSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["include"]
    search_fields = ["include"]
    
    
class IncludeDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Include.objects.all()
    serializer_class = IncludeSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["include"]


class CommentListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["post", "name", "description"]
    search_fields = ["post", "name", "description"]


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["post", "name", "description"]


class Things_to_knowListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Things_to_know.objects.all()
    serializer_class = Things_to_knowSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["title", "descriptions1"]
    search_fields = ["title",  "descriptions1"]


class Things_to_knowDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Things_to_know.objects.all()
    serializer_class = Things_to_knowSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["title", "guests", "descriptions1"]


class Experiences_listListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Experiences_list.objects.all()
    serializer_class = Experiences_listSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["title", "person_cost"]
    search_fields = ["title", "person_cost"]


class Experiences_listDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Experiences_list.objects.all()
    serializer_class = Experiences_listSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["title", "person_cost"]




class Experiences_descriptionsListAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Experiences_list.objects.all()
    serializer_class = Experiences_descriptionsSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["title", "descriptions1"]
    search_fields = ["title", "descriptions1"]


class Experiences_descriptionsDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Experiences_list.objects.all()
    serializer_class = Experiences_descriptionsSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    search_fields = ["title", "descriptions1"]






















































