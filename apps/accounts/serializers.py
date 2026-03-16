from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.accounts.models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 
            'name', 
            'bio', 
            'date_of_birth', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'email', 
            'is_active', 
            'is_admin', 
            'is_verified', 
            'verified_at', 
            'date_joined', 
            'last_login', 
            'profile'
        ]
        read_only_fields = [
            'is_active', 
            'is_admin', 
            'is_verified', 
            'verified_at', 
            'date_joined', 
            'last_login'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data.get('password')
        )
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance