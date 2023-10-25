from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from country.models import *


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]


class AuthorSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Author
        fields = "__all__"


class HotelInCitySerializer(ModelSerializer):

    class Meta:
        model = HotelInCity
        fields = "__all__"


class CountrySerializer(ModelSerializer):
    hotel_obj = HotelInCitySerializer(source='hotelincity_set', many=True, read_only=True)
    
    class Meta:
        model = Country
        fields = "id","city_name", "properties", "hotel_obj"


class InformationSerializer(ModelSerializer):
    
    class Meta:
        model = Information
        fields = "__all__"
        
        
class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        

class HotelInCityCostSerializer(ModelSerializer):

    class Meta:
        model = HotelInCityCost
        fields = "room_price_per_day", "room_check_in", "day", "service_charge", "total_cost"
        
        
class HotelInCitySerializer(ModelSerializer):
    comment_obj = CommentSerializer(source='comment_set', many=True, read_only=True)
    information_obj = InformationSerializer(source='information_set', many=True, read_only=True)
    hotel_in_city_cost_obj = HotelInCityCostSerializer(source='hotel_set', many=True, read_only=True)
    
    class Meta:
        model = HotelInCity
        fields = "id", "city", "title", "guests", "beds", "baths", "bathrooms", "stay_information", "information_obj", 'hotel_in_city_cost_obj', "comment_obj"