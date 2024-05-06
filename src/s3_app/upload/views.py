from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views import View

from utils.s3_client import *
from django.views.decorators.csrf import csrf_exempt
from .models import Document

class Service:
    def getAll():
        documents = Document.objects.all()
        return documents
    def deleteDocument(documentName):
        document = Document.objects.get(documentName=documentName)
        document.delete()
        return True

class IndexView(View):
    def get(self, request):
        # read the Documents Table and return
        documents = Service.getAll()
        return render(request, 'index.html',{'documents' : documents})
    
class UploadFileView(View):
    @csrf_exempt
    def post(self, request):
        uploaded_file = request.FILES['file']
        result = uploadDoc(uploaded_file)
        
        if (result):
            # store the file name on the database and send the 
            document = Document(documentName=result,createdBy='userId')
            document.save()
            return HttpResponse(200,'File Created Successfully')
        return HttpResponse(400,"file not uploaded")
    
class DownloadFileView(View):
    def post(self, request):
        data = json.loads(request.body)
        document = data['fileName']
        presigned_url = generatePresignedURL(document)
        return JsonResponse({ "presigned_url" : presigned_url})
    
class DeleteFileView(View):
    def post(self, request):
        data = json.loads(request.body)
        document = data['fileName']
        result = delete_file(document)
        if (result):
            Service.deleteDocument(document)
            return HttpResponse(200,'File Deleted Successfully')
        return HttpResponse(400,"file not deleted")
    
