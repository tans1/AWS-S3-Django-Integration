from django.db import models

# Create your models here.

class Document(models.Model):
    documentName = models.TextField()
    createdBy = models.CharField(max_length=100) #userId
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    