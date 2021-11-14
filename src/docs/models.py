from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=100, null=False)
    student_id = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=100,  null=True)
    validation_error = models.CharField(max_length=200,  null=True)

class DocumentType(models.Model):
    label = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)

class CourseRunDocType(models.Model):
    course_id = models.UUIDField(null=False)
    course_run_key = models.CharField(max_length=100, null=False)
    doc_types = models.CharField(max_length=200)