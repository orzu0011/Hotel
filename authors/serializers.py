# from rest_framework import serializers
# from .models import User

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=66, min_length=8, write_only=True)
    
#     class Meta:
#         model = User
#         fields = ('email', 'username', 'password')
        
#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         username = attrs.get('username', '')
        
#         if not username.isalnum():
#             raise serializers.ValidationError(
#                 'The username should only contain alphanumeric characters'
#             )
#             return attrs
        
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)









# # class UserSerializer(serializers.ModelSerializer):
# #     password = serializers.CharField(max_length=100, min_length=8, write_only=True)
# #     email = serializers.EmailField(max_length=100)
# #     first_name = serializers.CharField(max_length=255)
# #     last_name = serializers.CharField(max_length=255)
    
# #     class Meta:
# #         model = User
# #         fields = ["username", "first_name", "last_name",  "email", "password"]
        
        
# #     def validate(self, attrs):
# #         email = attrs.get('email', '')
# #         if User.objects.filter(email=email).exists():
# #             raise serializers.ValidationError({'email': ('Email is already in use')})
# #         return super().validate(attrs)
# #     def create(self, validated_data):
# #         return User.objects.create_user(**validated_data)