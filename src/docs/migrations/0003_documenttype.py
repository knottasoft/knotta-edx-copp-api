# Generated by Django 3.2.3 on 2021-10-09 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_auto_20210911_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
