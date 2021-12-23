from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

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

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

class DocumentArchive(models.Model):
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

    class Meta:
        verbose_name = 'Архивный документ'
        verbose_name_plural = 'Архивные документы'


class DocumentType(models.Model):
    label = models.CharField(max_length=100, null=False, verbose_name='Название документа')
    value = models.CharField(max_length=100, null=False, verbose_name='Системное имя')
    description = models.CharField(max_length=250, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'

class CourseRunDocType(models.Model):
    course_id = models.UUIDField(null=False)
    course_run_key = models.CharField(max_length=100, null=False)
    doc_types = models.CharField(max_length=200)

@receiver(post_save, sender=Document)
def copy_to_archive(sender, instance=None, created=False, **kwargs):
    # avoid recursion

    doc = archive_document_get_or_create(instance.id)

    doc.name = instance.name
    doc.student_id = instance.student_id
    doc.description = instance.description
    doc.date_create = instance.date_create
    doc.expiry_date = instance.expiry_date
    doc.validation_error = instance.validation_error
    doc.status = instance.status
    doc.email = instance.email
    doc.student_fio = instance.student_fio

    doc.save()

def archive_document_get_or_create (id):
    try:
        return DocumentArchive.objects.get(pk=id)
    except DocumentArchive.DoesNotExist:
        doc = DocumentArchive()
        doc.id = id
        return doc
