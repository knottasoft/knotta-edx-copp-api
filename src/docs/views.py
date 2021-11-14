from src.docs.serializers import DocumentSerializer, DocumentSerializerWithFiles, DocumentTypeSerializer, CourseRunDocTypeSerializer
from src.docs.models import Document, DocumentType, CourseRunDocType
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permissions = {'default': (IsAuthenticated)}

    def list(self, request, *args, **kwargs):
        sid = request.query_params.get('sid')
        queryset = Document.objects.all()

        if sid:
            queryset = queryset.filter(student_id=sid)

        serializer = DocumentSerializerWithFiles(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class DocumentTypeViewset(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
    permissions = {'default': (IsAuthenticated)}

    def list(self, request, *args, **kwargs):
        queryset = DocumentType.objects.all()
        serializer = DocumentTypeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CourseRunDocTypeViewset(viewsets.ModelViewSet):
    queryset = CourseRunDocType.objects.all()
    serializer_class = CourseRunDocTypeSerializer
    permissions = {'default': (IsAuthenticated)}

    def list(self, request, *args, **kwargs):
        course_id = request.query_params.get('course_id')
        course_run_key = request.query_params.get('course_run_key')
        
        queryset = CourseRunDocType.objects.all()
        
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        if course_run_key:
            queryset = queryset.filter(course_run_key=course_run_key)

        serializer = CourseRunDocTypeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        CourseRunDocType.objects.update_or_create(
            course_id = request.data['course_id'],
            course_run_key = request.data['course_run_key'],
            defaults = { 'doc_types' : request.data['doc_types']}
        )
        return Response()
#return super().create(request, *args, **kwargs)