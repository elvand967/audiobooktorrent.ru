# D:\Python\myProject\audiobooktorrent.ru\app\main\models.py

from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.urls import reverse, NoReverseMatch

from main.utilities import get_img_file_path

GRID_CHOICES = [
    ('r1c1', '1-й ряд, 1-ая колонка из 4-х',),
    ('r1c2', '1-й ряд, 2-ая колонка из 4-х',),
    ('r1c3', '1-й ряд, 3-ая колонка из 4-х',),
    ('r1c4', '1-й ряд, 4-ая колонка из 4-х',),
    ('r2c1', '2-й ряд',),
    ('r3c1', '3-й ряд',),
    ('r4c1', '4-й ряд',),
    ('seo', 'SEO обеспечение',),
]


class CategoriesFooter(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="slug")
    grid_class = models.CharField(max_length=50, choices=GRID_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группу (Категорию)"
        verbose_name_plural = "Группы (Категории)"


class InternalURLField(models.CharField):
    ''' Контроль ввода имени внутренней ссылки '''
    description = "Internal URL field"

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 255)
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if not value:
            return value
        try:
            reverse(value)
        except NoReverseMatch:
            raise ValidationError("Invalid internal URL: {}".format(value))
        return value


class FooterLinks(models.Model):
    cat_footer = models.ForeignKey("CategoriesFooter", on_delete=models.CASCADE, related_name="basement_group",
                                   verbose_name="Категория Footer")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=50, blank=True, null=True, verbose_name="slug",
                            help_text='Если "Внутренняя ссылка" не определена и указан slug, будет применен абсолютный путь infopage/"slug:slug"/')
    clue = models.CharField(max_length=255, blank=True, null=True, verbose_name="Подсказка")
    internal_link = InternalURLField(blank=True, null=True, verbose_name="Относительная ссылка",
                                     help_text="Относительные ссылки должны соответствовать urls.name моделей")
    url = models.URLField(blank=True, null=True, verbose_name="Внешняя ссылка")
    icon = models.CharField(max_length=100, blank=True, null=True, )

    def clean(self):
        ''' Валидатор корректного ввода внутренней ссылки '''
        if self.internal_link:
            try:
                reverse_value = reverse(self.internal_link)
            except NoReverseMatch:
                raise ValidationError(
                    "Не корректный ввод имени URL, внутренней относительной ссылки: {}".format(self.internal_link))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse('infopage', kwargs={'slug': self.slug})
        else:
            return

    class Meta:
        verbose_name = "Ссылку, контекст"
        verbose_name_plural = "Ссылки, контекст"


IMAGE_WIDTH = [
    ('img25', 'Ширина изображения 25%',),
    ('img30', 'Ширина изображения 30%',),
    ('img50', 'Ширина изображения 50%',),
    ('img100', 'Ширина изображения 100%',),
]

IMAGE_POSITION = [
    ('img_left', 'Изображение по левому краю',),
    ('img_right', 'Изображение по правому краю',),
]

class ContentPage(models.Model):
    footer_links = models.ForeignKey("FooterLinks", on_delete=models.CASCADE, related_name="content_links",
                                     verbose_name="Информационная страница")
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Тема/Вопрос")
    display_title = models.BooleanField(default=False, verbose_name="Отображать заголовок")
    text = models.TextField(blank=True, null=True, verbose_name="Текст")
    picture = models.ImageField(
        upload_to=get_img_file_path,  # метод сохранения по пути media/files_picture/main/
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    image_width = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ширина изображения",
                                   choices=IMAGE_WIDTH, default='img25')
    image_position = models.CharField(max_length=255, blank=True, null=True, verbose_name="Позиция изображения",
                                      choices=IMAGE_POSITION, default='img_left')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Контент ссылки"
        verbose_name_plural = "Контент ссылок"
