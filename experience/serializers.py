from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from experience.models import *
from drf_extra_fields.fields import Base64ImageField


class ExperiencesCostSerializer(ModelSerializer):
    class Meta:
        model = ExperiencesCost
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data['guests'] = validated_data['Adults'] + validated_data['Children'] + validated_data['Infants']
        validated_data['guests_main'] = (validated_data['guests'] - validated_data['Infants'])
        validated_data['total_cost'] = validated_data['guests_main'] * validated_data['Infants'] + validated_data['service_charge'] + validated_data['Infants']
        validated_data['discount'] = validated_data['discount'] * 100 / validated_data['guests_main']


        return super().create(validated_data)
    

class IncludeSerializer(ModelSerializer):
    class Meta:
        model = Include
        fields = "__all__"
        
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        
        
class Things_to_knowSerializer(ModelSerializer):
    class Meta:
        model = Things_to_know
        fields = "__all__"
        
        
class Experiences_descriptionsSerializer(ModelSerializer):
    class Meta:
        model = Experiences_descriptions
        fields = "__all__"
        
class ExperiencesSerializer(ModelSerializer):
    comment_obj = CommentSerializer(source='comment_set', many=True, read_only=True)
    experiences_descriptions_obj = Experiences_descriptionsSerializer(source='experiences_descriptions_set', many=True, read_only=True)
    include_obj = IncludeSerializer(source='include_set', many=True, read_only=True)
    things_to_know_obj = Things_to_knowSerializer(source='things_to_know_set', many=True, read_only=True)
    
    class Meta:
        model = Experiences
        fields = "id","title", "author", "hour", "number_of_people", "language", "comment_obj", "experiences_descriptions_obj", "include_obj", "things_to_know_obj"
    
        
class Experiences_listSerializer(ModelSerializer):
    experiences_obj = ExperiencesSerializer(source='experiences_set', many=True, read_only=True)

    class Meta:
        model = Experiences_list
        fields = "id", "title", "person_cost", "experiences_obj"