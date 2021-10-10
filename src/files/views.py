from rest_framework import viewsets, mixins
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from .serializers import FileSerializer
from .models import File
'''
class FilesViewset(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, 
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
   '''
class FilesViewset(viewsets.ModelViewSet):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    parser_classes = (MultiPartParser, FormParser)
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permissions = {'default': (IsAuthenticated)}

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request):
        queryset = File.objects.all()
        serializer = FileSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
