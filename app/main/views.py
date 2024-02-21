# D:\Python\myProject\bookshelves\app\main\views.py
from django.forms import model_to_dict
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import View

from main.forms import ContactForm
from main.models import FooterLinks


class InfoPageDetailView(View):
    template_name = "main/info_page_detail.html"

    def get(self, request, slug):
        infopage = get_object_or_404(FooterLinks, slug=slug)
        return render(request, self.template_name, {"infopage": infopage})

# class InfoPageDetailView(View):
#     template_name = "main/info_page_detail.html"
#
#     def get(self, request, slug):
#         # Получаем объект FooterLinks по его slug
#         footer_link = get_object_or_404(FooterLinks, slug=slug)
#
#         # Получаем все связанные объекты ContentPage для этого FooterLinks
#         content_pages = footer_link.content_links.all()
#         # Удалим ненужные поля модели
#         # Преобразование каждого объекта ContentPage в словарь
#         content_pages_data = []
#         for page in content_pages:
#             page_data = model_to_dict(page)  # Преобразование объекта в словарь
#             if not page.display_title:  # Удаление ключей, если display_title=False
#                 del page_data['title']
#                 del page_data['display_title']
#             if not page.picture:
#                 del page_data['picture']  # Удаление ключа 'picture', если picture=None
#                 del page_data['image_width']  # Удаление ключа 'image_width', если picture=None
#                 del page_data['image_position']  # Удаление ключа 'image_position', если picture=None
#             content_pages_data.append(page_data)
#
#         # Собираем все необходимые данные для передачи в шаблон
#         context = {
#             'footer_link': footer_link,
#             'content_pages_data': content_pages_data,
#         }
#
#         # Отображаем шаблон, передавая контекст
#         return render(request, self.template_name, context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def about(request):
    data = {
        'title': 'О сайте',
        'text': 'На этой странице информация о сайте',
    }
    return render(request, 'main/about.html', context=data)


def fag(request):
    data = {
        'title': 'FAG',
        'text': 'Часто задаваемые вопросы',
    }
    return render(request, 'main/fag.html', context=data)


def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ContactForm()

    data = {
        'title': 'Обратная связь',
        'form': form,
    }
    return render(request, 'main/feedback.html', context=data)


def chat(request):
    data = {
        'title': 'Общий чат',
        'text': 'Общий чат сайта',
    }
    return render(request, 'main/chat.html', context=data)


