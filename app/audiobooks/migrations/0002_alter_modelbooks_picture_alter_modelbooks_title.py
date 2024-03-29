# Generated by Django 4.1.10 on 2024-02-18 00:10

import audiobooks.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiobooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelbooks',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=audiobooks.utilities.get_picture_file_path, verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='modelbooks',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Название аудиокниги'),
        ),
    ]
