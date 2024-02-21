# D:\Python\myProject\bookshelves\app\main\templatetags\main_tags.py

from django import template
from main.models import FooterLinks

register = template.Library()


@register.simple_tag(name="horizontal_menu")
def get_horizontal_menu():
    """Функция def get_horizontal_menu(), которая будет возвращать
    список ссылок главного меню при вызове нашего тега из шаблона.
    Свяжем эту функцию с тегом, или, превратим эту функцию в тег,
    используя специальный декоратор
    `@register.simple_tag(name='horizontal_menu')`,
     доступный через переменную `register`."""
    menu = [
        {
            "title": "Главная",
            "url_name": "home",
            "link_hint": "Аудиокниги с книжной полки",
        },
        {
            "title": "О нас",
            "url_name": "about",
            "link_hint": "О нас, контакты, другая информация",
        },
        {"title": "FAG", "url_name": "fag", "link_hint": "Часто задаваемые вопросы"},
        {
            "title": "Обратная связь",
            "url_name": "feedback",
            "link_hint": "Отправить сообщение администрации сайта",
        },
        {"title": "Чат", "url_name": "chat", "link_hint": "Войти в общий чат сайта"},
    ]
    # menu = ["О сайте", "Добавить книгу", "Обратная связь", "Войти"]
    return menu


''' Меню футера. Контекст передоваемых в одноименные словари ссылок (r1c1, и т.д.)
 формируем на основании фильтра по полю `grid_class` модели `CategoriesFooter`'''
@register.inclusion_tag('main/templatetags/footer.html')
def render_footer():
    r1c1 = FooterLinks.objects.filter(cat_footer__grid_class='r1c1')  # `Главная`
    r1c2 = FooterLinks.objects.filter(cat_footer__grid_class='r1c2')  # `Навигация`
    r1c3 = FooterLinks.objects.filter(cat_footer__grid_class='r1c3')  # `Контактная информация`
    r1c4 = FooterLinks.objects.filter(cat_footer__grid_class='r1c4')  # `Политика и правила`
    r2c1 = FooterLinks.objects.filter(cat_footer__grid_class='r2c1')  # `иконки-ссылки на социальные сети`
    r3c1 = FooterLinks.objects.filter(cat_footer__grid_class='r3c1')  # `Поддержать проект`
    r4c1 = FooterLinks.objects.filter(cat_footer__grid_class='r4c1')  # `Copyright - авторское право`

    data = {
        'r1c1': r1c1,  # Контекст (ссылки) для grid-ячейки footer класса `r1c1`
        'r1c2': r1c2,  # ...
        'r1c3': r1c3,
        'r1c4': r1c4,
        'r2c1': r2c1,
        'r3c1': r3c1,
        'r4c1': r4c1,
    }

    return data