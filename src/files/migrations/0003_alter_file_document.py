# Generated by Django 3.2.3 on 2021-10-06 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_auto_20210911_0733'),
        ('files', '0002_file_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='docs.document'),
        ),
    ]