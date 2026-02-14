from django.urls import path
from .views import FileUploadView, FileDeleteView

urlpatterns = [
    path('files/', FileUploadView.as_view(), name='file-upload'),
    path('files/<int:pk>/', FileDeleteView.as_view(), name='file-delete'),
]

