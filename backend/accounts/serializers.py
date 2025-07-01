from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework import serializers
from rest_framework.serializers import CharField, ModelSerializer, ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        token['profile_image'] = user.profile_image.url if user.profile_image else None
        token['id'] = user.id
        token['is_admin'] = user.is_admin
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'name']


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True,
        required=False,
        write_only=True
    )
    permission_details = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'email', 'password', 'profile_image',
            'date_joined', 'is_active', 'is_staff','is_admin',
            'permissions', 'permission_details'
        ]

    def get_permission_details(self, user):
        # get strings like "app_label.codename"
        perm_strings = user.get_all_permissions()
        # split and find Permission objects
        perms = Permission.objects.filter(
            content_type__app_label__in=[s.split('.')[0] for s in perm_strings],
            codename__in=[s.split('.')[1] for s in perm_strings]
        )
        return PermissionSerializer(perms, many=True).data

    def validate(self, data):
        pw = data.get('password', None)
        if pw and (len(pw) < 6 or len(pw) > 12):
            raise ValidationError({'password': 'Password between 6‑12 chars'})
        return data

    def create(self, validated_data):
        perms = validated_data.pop('permissions', [])
        email = validated_data.pop('email')
        pw = validated_data.pop('password')
        user = self.Meta.model.objects.create_user(email, pw, **validated_data)
        if perms:
            user.user_permissions.set(perms)
        return user

    def update(self, instance, validated_data):
        perms = validated_data.pop('permissions', None)
        for k, v in validated_data.items():
            if k == 'profile_image':
                instance.profile_image.delete(save=False)
            if k == 'password':
                instance.set_password(v); continue
            setattr(instance, k, v)
        instance.save()
        if perms is not None:
            instance.user_permissions.set(perms)
        return instance
