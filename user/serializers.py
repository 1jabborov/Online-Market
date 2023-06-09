import base64
import io
from django.core.files import File
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import User
from rest_framework.validators import UniqueValidator

# Create your serializers here.

def password_validator(value):
    if len(value) < 8 and value.is_numeric():
        raise ValidationError("This is bad password")
    else:
        return True


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator, ),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('password',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    avatar = serializers.CharField(required=False)

    def create(self, validated_data):
        password = self.initial_data.get('password', False)
        avatar = self.initial_data.get('avatar', False)
        if not password:
            raise ValueError('error')
        if self.initial_data.get('avatar', False):
            validated_data.pop('avatar')
        instance = super().create(validated_data)
        instance.password = make_password(password)
        if avatar:
            p = base64.b64decode(self.initial_data.get('avatar', False))
            img = io.BytesIO()
            img.write(p)
            instance.avatar = File(name=f"avatar_{instance.id}", file=img)
        instance.is_active = False
        instance.save()
        return instance

    class Meta:
        model = User
        fields = 'name', 'surname', 'avatar', 'email', 'username', 'is_active', 'birthday', \
            'user_type',


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
