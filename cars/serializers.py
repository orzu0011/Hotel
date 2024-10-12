from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from cars.models import *
from drf_extra_fields.fields import Base64ImageField


class CarAdvantagesSerializer(ModelSerializer):
    class Meta:
        model = CarAdvantages
        fields = "__all__"


class Car_descriptionSerializer(ModelSerializer):
    class Meta:
        model = Car_description
        fields = "__all__"


class IncludeSerializer(ModelSerializer):
    class Meta:
        model = Include
        fields = "__all__"


class CarOwnerSerializer(ModelSerializer):
    class Meta:
        model = CarOwner
        fields = "__all__"

        
class CarInformationSerializer(ModelSerializer):
    class Meta:
        model = CarInformation
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = 'post', 'name', 'description', 'created'



class CarCostSerializer(ModelSerializer):
    class Meta:
        model = CarCost
        fields = "__all__"
        
    def create(self, validated_data):
        a = validated_data['car_drop_off'] - validated_data['car_pick_up'] 
        validated_data['day'] = a.days
        
        validated_data['total_cost'] = validated_data['day'] * validated_data['car_price_per_day']
        validated_data['discount'] = validated_data['discount'] * 100 / validated_data['total_cost']
        return super().create(validated_data)
    
    


    

class CarSerializer(ModelSerializer):
    cost_obj = CarCostSerializer(source='carcost_set', many=True, read_only=True)
    comment_obj = CommentSerializer(source='comment_set', many=True, read_only=True)
    car_information_obj = CarInformationSerializer(source='car_information_set', many=True, read_only=True)
    car_advantage_obj = CarAdvantagesSerializer(source='caradvantages_set', many=True, read_only=True)
    car_description = Car_descriptionSerializer(source='car_description_set', many=True, read_only=True)
    include_obj = IncludeSerializer(source='include_set', many=True, read_only=True)
    picture = Base64ImageField()

    class Meta:
        model = Car
        fields = "id", 'name', 'car_owner', 'bags', 'picture', 'cost_obj', 'car_advantage_obj', 'include_obj', 'car_description', 'comment_obj', 'car_information_obj'


class CarsSerializer(ModelSerializer):
    car_obj = CarSerializer(source='car_set', many=True, read_only=True)
    picture = Base64ImageField()
    class Meta:
        model = Cars
        fields = 'id', 'cars_name', 'seats', 'choice', 'picture', 'price_days', 'car_obj'