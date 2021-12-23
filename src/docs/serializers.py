from django.db.models import fields
from rest_framework import serializers, permissions
from .models import Document, DocumentArchive, DocumentType, CourseRunDocType
from src.files.serializers import FileSerializer

class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = ('name', 'description', 'date_create', 'student_id', 'id', 'status', 'expiry_date', 'validation_error', "email", "student_fio")

class DocumentSerializerWithFiles(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta():
        model = Document
        fields = ('name', 'description', 'date_create', 'student_id', 'files', 'id', 'status', 'expiry_date', 'validation_error', "email", "student_fio")

class DocumentArchiveSerializer(serializers.ModelSerializer):
    class Meta():
        model = DocumentArchive
        fields = ('name', 'description', 'date_create', 'student_id', 'id', 'status', 'expiry_date', 'validation_error', "email", "student_fio")

class DocumentArchiveSerializerWithFiles(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta():
        model = DocumentArchive
        fields = ('name', 'description', 'date_create', 'student_id', 'files', 'id', 'status', 'expiry_date', 'validation_error', "email", "student_fio")


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta():
        model = DocumentType
        fields = ('label', 'value', 'description')
    
class CourseRunDocTypeSerializer(serializers.ModelSerializer):
    class Meta():
        model = CourseRunDocType
        fields = ('course_id', 'course_run_key', 'doc_types')