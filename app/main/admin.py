# D:\Python\myProject\bookshelves\app\main\admin.py
from django import forms
from django.contrib import admin
from .management.commands.backup_copy_db import database_backup
from .models import CategoriesFooter, ContentPage, FooterLinks


def backup_database(modeladmin, request, queryset):
    database_backup()
# Set a short description for the action / Задайте краткое описание действия
backup_database.short_description = "Резервная копия Database"


class CategoriesFooterAdmin(admin.ModelAdmin):
    # Add the custom action to the model admin / Добавьте настраиваемое действие в администратора модели.
    list_display = ('grid_class', 'title', 'slug',)
    list_display_links = ('grid_class', 'title',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
# Register your model and its admin / Зарегистрируйте свою модель и ее администратора
admin.site.register(CategoriesFooter, CategoriesFooterAdmin)


class ContentPageInline(admin.StackedInline):
    ''' Inline class for ContentInfoPageInline
    class ContentInfoPageInline(admin.TabularInline):  # поля в линию
    class ContentInfoPageInline(admin.StackedInline):  # поля в столбец '''
    model = ContentPage
    extra = 1  # Количество дополнительных блоков для отображения

class FooterLinksAdmin(admin.ModelAdmin):
    # Add the custom action to the model admin / Добавьте настраиваемое действие в администратора модели.
    list_display = ('cat_footer', 'title', 'clue')
    list_display_links = ('title',)  # поля-ссылки на экземпляр модели
    search_fields = ('title',)  # Поля, по которым будет производиться поиск
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('cat_footer',)  # Добавим фильтры по полям
    # встраиваем связанную модель
    inlines = [ContentPageInline]  # Добавляем связанные объекты ContentPage в админ-панель форму


# Register your model and its admin / Зарегистрируйте свою модель и ее администратора
admin.site.register(FooterLinks, FooterLinksAdmin)