from django.db.models import fields
from rest_framework import serializers, permissions
from .models import Document, DocumentType, CourseRunDocType
from src.files.serializers import FileSerializer

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = ('name', 'description', 'date_create', 'student_id', 'id', 'status', 'expiry_date', 'validation_error')

class DocumentSerializerWithFiles(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta():
        model = Document
        fields = ('name', 'description', 'date_create', 'student_id', 'files', 'id', 'status', 'expiry_date', 'validation_error')

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta():
        model = DocumentType
        fields = ('label', 'value', 'description')
    
class CourseRunDocTypeSerializer(serializers.ModelSerializer):
    class Meta():
        model = CourseRunDocType
        fields = ('course_id', 'course_run_key', 'doc_types')