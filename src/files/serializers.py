from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'thumbnail', 'created_at', 'document', 'id')

    def create(self, validated_data):
        return super().create(validated_data)

class FileArchiveSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('file', 'thumbnail', 'created_at', 'document', 'id')

    def create(self, validated_data):
        return super().create(validated_data)
