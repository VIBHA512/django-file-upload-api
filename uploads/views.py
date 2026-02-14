from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import FileSerializer


class FileUploadView(generics.ListCreateAPIView):

    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)


class FileDeleteView(generics.DestroyAPIView):

    queryset = UploadedFile.objects.all()
    serializer_class = FileSerializer
