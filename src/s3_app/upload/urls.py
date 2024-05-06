from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('upload/', UploadFileView.as_view()),
    path('download/', DownloadFileView.as_view()),
    path('delete/', DeleteFileView.as_view())
    
]
