from rest_framework import serializers
from .models import AcademicBackground


class AcademicBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBackground
        fields = ('id', 'profile', 'course', 'institution', 'start_date', 'end_date', 'description', 'created_at')
        read_only_fields = ('created_at',)