from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=100, null=False)
    student_id = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add=True)

class DocumentType(models.Model):
    label = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)