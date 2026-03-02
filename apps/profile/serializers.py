<<<<<<< HEAD
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'photo', 'role', 'description', 'email', 'linkedin', 'github', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
=======
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'photo', 'role', 'description', 'email', 'linkedin', 'github', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
>>>>>>> origin/main
