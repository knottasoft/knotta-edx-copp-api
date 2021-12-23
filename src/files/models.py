from django.db import models
from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from easy_thumbnails.exceptions import EasyThumbnailsError
from easy_thumbnails.files import get_thumbnailer
from PIL import UnidentifiedImageError


class File(models.Model):
    THUMBNAIL_SIZE = (360, 360)

    file = models.FileField(blank=False, null=False)
    thumbnail = models.ImageField(blank=True, null=True)
    document = models.ForeignKey('docs.Document', related_name='files', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class FileArchive(models.Model):
    THUMBNAIL_SIZE = (360, 360)

    file = models.FileField(blank=False, null=False)
    thumbnail = models.ImageField(blank=True, null=True)
    document = models.ForeignKey('docs.DocumentArchive', related_name='files', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(pre_delete, sender=FileArchive)
def auto_delete_archive_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()

    if instance.thumbnail:
        instance.thumbnail.delete()

@receiver(post_save, sender=File)
def generate_thumbnail(sender, instance=None, created=False, **kwargs):
    # avoid recursion
    if created is False:
        return

    thumbnailer = get_thumbnailer(instance.file.name, relative_name='thumbnail')
    try:
        thumbnail = thumbnailer.get_thumbnail({'size': File.THUMBNAIL_SIZE}, save=False)
    except (UnidentifiedImageError, EasyThumbnailsError):
        return
    else:
        instance.thumbnail.save(name=f'small_{instance.file.name}', content=thumbnail)


@receiver(post_save, sender=File)
def copy_to_archive(sender, instance=None, created=False, **kwargs):
    if created is False:
        return

    file = FileArchive()
    file.id = instance.id
    file.file = instance.file
    file.thumbnail = instance.thumbnail
    file.document_id = instance.document_id
    file.created_at = instance.created_at

    file.save()
