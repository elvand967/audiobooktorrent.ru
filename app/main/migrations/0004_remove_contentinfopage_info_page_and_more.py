# Generated by Django 4.1.10 on 2024-02-19 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_categoriesfooter_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentinfopage',
            name='info_page',
        ),
        migrations.RemoveField(
            model_name='infopage',
            name='category_info',
        ),
        migrations.AlterModelOptions(
            name='footerlinks',
            options={'verbose_name': 'Ссылку, контекст', 'verbose_name_plural': 'Ссылки, контекст'},
        ),
        migrations.AlterField(
            model_name='categoriesfooter',
            name='grid_class',
            field=models.CharField(choices=[('r1c1', '1-й ряд, 1-ая колонка из 4-х'), ('r1c2', '1-й ряд, 2-ая колонка из 4-х'), ('r1c3', '1-й ряд, 3-ая колонка из 4-х'), ('r1c4', '1-й ряд, 4-ая колонка из 4-х'), ('r2c1', '2-й ряд'), ('r3c1', '3-й ряд'), ('r4c1', '4-й ряд'), ('seo', 'SEO обеспечение')], max_length=50),
        ),
        migrations.AlterField(
            model_name='footerlinks',
            name='slug',
            field=models.SlugField(blank=True, help_text='Если "Внутренняя ссылка" не определена и указан slug, будет применен абсолютный путь infopage/"slug:slug"/', null=True, verbose_name='slug'),
        ),
        migrations.DeleteModel(
            name='CategoriesInfo',
        ),
        migrations.DeleteModel(
            name='ContentInfoPage',
        ),
        migrations.DeleteModel(
            name='InfoPage',
        ),
    ]