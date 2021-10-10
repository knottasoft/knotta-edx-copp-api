from src.docs.serializers import DocumentSerializer, DocumentSerializerWithFiles, DocumentTypeSerializer
from src.docs.models import Document, DocumentType
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