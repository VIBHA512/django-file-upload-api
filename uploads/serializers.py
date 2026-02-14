from rest_framework import serializers
from .models import UploadedFile

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at']
