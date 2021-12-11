from django.core.exceptions import ValidationError
from django.db import models

class Document(models.Model):
    DOC_STATUS = (
        ('n', 'Нет статуса'),
        ('v', 'Проверен'),
        ('r', 'Возвращен'),
    )

    name = models.CharField(max_length=100, null=False, verbose_name='Наименование')
    student_id = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, verbose_name='Тип документа')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    expiry_date = models.DateField(null=True, verbose_name='Действителен до')
    validation_error = models.CharField(max_length=200,  null=True, blank=True, verbose_name='Замечания проверки')
    status = models.CharField(max_length=1, choices=DOC_STATUS, blank=True, default='n', verbose_name='Статус', help_text='Состояние проверки документа модератором')
    email = models.CharField(max_length=200, null=True, verbose_name='E-mail')
    student_fio = models.CharField(max_length=200, null=True, verbose_name='Студент')


class DocumentType(models.Model):
    label = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=True)

class CourseRunDocType(models.Model):
    course_id = models.UUIDField(null=False)
    course_run_key = models.CharField(max_length=100, null=False)
    doc_types = models.CharField(max_length=200)