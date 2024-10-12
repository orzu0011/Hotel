from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


# router = SimpleRouter()
# router.register(r'user_page', UserViewSet, basename="user_page")
# router.register(r'api_categories_avatar', AvatarUpdateView, basename="avatar_update_page")


urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'}), name="user_page"),
    path('api/categories/avatar/', AvatarUpdateView.as_view(), name='avatar-upload'),
]