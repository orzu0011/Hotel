import base64
import io
from django.contrib.auth.hashers import make_password
from django.core.files import File
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField
from User.models import User


def password_validator(value):
    if len(value) < 8:
        raise ValidationError("This is bad password")
    else:
        return True


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator, ),
        help_text='Leave empty if no change needed',
        style={'input_type': "password", 'placeholder': "Password"}
    )

    class Meta:
        model = User
        fields = ('password', )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.CharField()

    def create(self, validated_data):
        password = self.initial_data.get('password', False)

        p = base64.b64decode(self.initial_data.get('avatar', False))
        img = io.BytesIO()
        img.write(p)
        if not password:
            raise ValueError('error')
        validated_data.pop('avatar')
        instance = super().create(validated_data)
        instance.password = make_password(password)
        instance.is_active = False
        instance.avatar = File(name=f"avatar_{instance.id}", file=img)
        # instance.is_staff = True
        instance.save()
        return instance

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'avatar', 'email', 'username', 'birthday', 'phone', \
            'user_type'


class UserProfileSerializer(serializers.ModelSerializer):
    user_data = PrimaryKeyRelatedField(source="avatar", many=True, read_only=True)
    class Meta:
        model = User
        fields = ['avatar', 'user_data']