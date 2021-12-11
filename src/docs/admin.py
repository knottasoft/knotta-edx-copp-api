from django.contrib import admin
from django.db.models import fields

from src.docs.models import Document, DocumentType
from src.files.models import File

class DocFilesInline(admin.StackedInline):
    model = File
    extra = 0
    fields = ( 'file_preview', 'file')
    readonly_fields = ('file_preview', 'file')

    def file_preview(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" />', obj.thumbnail.url)
    
    file_preview.short_description = "Просмотр"

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    empty_value_display = "Нет замечаний"
    list_display = ("name", "doc_type", "email", "student_fio", "status", "expiry_date", "date_create")
    list_filter = ("status", )
    readonly_fields = ('doc_type', "email", "student_fio")
    fields = ("doc_type", "email", "student_fio", "name", "status", "expiry_date", "validation_error")
    inlines = [DocFilesInline]

    def doc_type(self, obj):
        result = DocumentType.objects.get(value=obj.description)
        return result.label

    doc_type.short_description = "Тип документа"