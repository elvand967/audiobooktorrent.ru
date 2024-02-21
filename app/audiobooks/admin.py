# D:\Python\myProject\bookshelves\app\audiobooks\admin.py

from django.contrib import admin
from .models import Author, Reader, Cycle, ModelSubcategories, ModelBooks, ModelCategories
from django.utils.safestring import mark_safe

@admin.register(ModelCategories)
class ModelCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', )  # сортируем по имени категории


@admin.register(ModelSubcategories)
class ModelSubcategoriesAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug')
    list_display_links = ('name', 'slug')  # поля-ссылки на экземпляр модели
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('category',)  # порядок сортировки


@admin.register(ModelBooks)
class ModelBooksAdmin(admin.ModelAdmin):
    # отображаемые поля в списке аудиокниг
    # list_display = ('category', 'book_subcategories', 'book_picture', 'title', 'authors', 'is_published')
    list_display = ('book_picture', 'title', 'brief_info', 'is_published',)
    list_display_links = ('book_picture', 'title',)  # поля-ссылки на экземпляр модели
    list_editable = ('is_published',)  # Обеспечим возможность редактирования прямо в таблице книг
    # search_fields = ('title', 'authors',)  # Поля, по которым будет производиться поиск
    search_fields = ('title',)  # Поля, по которым будет производиться поиск
    list_filter = ('is_published', 'time_update',)  # Добавим фильтры по полям

    prepopulated_fields = {'slug': ('title',)}  # ???
    filter_horizontal = ('book_subcategories', 'authors', 'readers',)
    ordering = ('book_subcategories',)  # порядок сортировки

    # Порядок и список редактируемых полей при редактировании экземпляра модели
    # fields = ('title', 'authors', 'is_published', 'category', 'book_subcategories', 'book_picture',)

    ''' description="Обложка", - Константа `description` значение = Заголовок столбца'''
    @admin.display(description="Обложка")
    def book_picture(self, book: ModelBooks):
        if book.picture:
            return mark_safe(f"<img src='{book.picture.url}' width=50>")
        return "Без обложки"


    ''' description="Описание", - Константа `description` значение = Заголовок столбца
        ordering='description', - возможность сортировки по значению'''
    @admin.display(description="Описание", ordering='description',)
    def brief_info(self, book_txt: ModelBooks):
        return f"{len(book_txt.description)} символов."


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)  # сортируем по имени автора


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')
    search_fields = ('name',)  # Поля, по которым будет производиться поиск
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)  # Сортируем по названию цикла


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)  # Сортируем по имени чтеца


admin.site.site_header = 'Книжные полки'
admin.site.site_title = 'Аудиокниги, скачать торрентом'
