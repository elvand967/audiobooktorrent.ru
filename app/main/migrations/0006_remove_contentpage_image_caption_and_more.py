# Generated by Django 4.1.10 on 2024-02-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_categoriesfooter_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentpage',
            name='image_caption',
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='image_position',
            field=models.CharField(blank=True, choices=[('img_left', 'Изображение по левому краю'), ('img_right', 'Изображение по правому краю')], default='img_left', max_length=255, null=True, verbose_name='Позиция изображения'),
        ),
    ]
