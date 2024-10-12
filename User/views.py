from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import generics
from .models import User, ViewPermission
from .serializers import UserSerializer, PasswordSerializer
from .serializers import UserProfileSerializer


class UserViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # parser_classes = (MultiPartParser, FormParser)
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'option']

    @action(detail=True, methods=['POST'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': "password set"})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["POST"], permission_classes=[])
    def login(self, request, pk=None):
        queryset = self.get_queryset()
        serializer = request.data
        try:
            user = queryset.get(username=serializer['username'])
            if not user.check_password(serializer['password']):
                return Response({'user': "password is invalid"}, status=412)
            elif not user.is_active:
                return Response({'user': "user is blocked", 'valid': False}, status=412)
            else:
                return Response({'username': user.username,
                                'role': user.user_type,
                                'fullname': user.get_full_name()})
        except User.DoesNotExist:
            return Response('user not found', status=status.HTTP_404_NOT_FOUND)


class AvatarUpdateView(generics.UpdateAPIView):
    users = UserViewSet()
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)