from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from country.models import *
from drf_extra_fields.fields import Base64ImageField

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]


class AuthorSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Author
        fields = "__all__"





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
    
    def create(self, validated_data):
        validated_data['total_cost'] = validated_data['room_price_per_day'] * validated_data['day'] + validated_data['service_charge']
        return super().create(validated_data)
    
        
class HotelInCitySerializer(ModelSerializer):
    comment_obj = CommentSerializer(source='comment_set', many=True, read_only=True)
    information_obj = InformationSerializer(source='information_set', many=True, read_only=True)
    hotel_in_city_cost_obj = HotelInCityCostSerializer(source='hotelincitycost_set', many=True, read_only=True)
    class Meta:
        model = HotelInCity
        fields = "id", "city", "title", "guests", "beds", "baths", "bathrooms", "stay_information", "information_obj", 'hotel_in_city_cost_obj', "comment_obj"
        
        
class CountrySerializer(ModelSerializer):
    hotel_obj = HotelInCitySerializer(source='hotelincity_set', many=True, read_only=True)
    picture = Base64ImageField()
    class Meta:
        model = Country
        fields = "id","city_name", "properties", 'picture' ,"hotel_obj"

