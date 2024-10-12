from django.urls import path
from experience.views import *



urlpatterns = [
   path("", Experiences_listListAPIView.as_view(), name="list"),
   path("<int:pk>", Experiences_listDetailAPIView.as_view(), name="detail"),
   path("experience", ExperiencesListAPIView.as_view(), name="about"),
   path("experience/<int:pk>", ExperiencesDetailAPIView.as_view(), name="about_detail"),
   path("description", Experiences_descriptionsListAPIView.as_view(), name="about"),
   path("description/<int:pk>", Experiences_descriptionsDetailAPIView.as_view(), name="about_detail"),
   path("comment", CommentListAPIView.as_view(), name="comment"),
   path("comment/<int:pk>", CommentDetailAPIView.as_view(), name="comment"),
   path("know", Things_to_knowListAPIView.as_view(), name="information"),
   path("know/<int:pk>", Things_to_knowDetailAPIView.as_view(), name="information_detail"),
   path("experiencecost", ExperiencesCostListAPIView.as_view(), name="HotelListAPIView"),
   path("experiencecost/<int:pk>", ExperiencesCostDetailAPIView.as_view(), name="HotelListAPIView"),
   
]