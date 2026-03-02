from rest_framework import serializers
from .models import Project, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('id', 'name', 'created_at')
        read_only_fields = ('created_at',)


class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True, read_only=True)
    technologies_ids = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Technology.objects.all(), source='technologies')

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'image', 'technologies', 'technologies_ids', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
