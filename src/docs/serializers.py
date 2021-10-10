from django.db.models import fields
from rest_framework import serializers, permissions
from .models import Document, DocumentType
from src.files.serializers import FileSerializer

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = ('name', 'description', 'date_create', 'student_id', 'id')

class DocumentSerializerWithFiles(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta():
        model = Document
        fields = ('name', 'description', 'date_create', 'student_id', 'files', 'id')

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta():
        model = DocumentType
        fields = ('label', 'value', 'description')