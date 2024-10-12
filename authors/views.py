# from django.shortcuts import render
# from rest_framework import generics
# from .serializers import *
# from rest_framework.response import Response
# from rest_framework import status


# class RegisterAPIView(generics.GenericAPIView):
#     serializer_class = RegisterSerializer 
    
#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=User)
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()

#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
    
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    