# D:\Python\myProject\bookshelves\app\main\urls.py

from django.urls import path
from . import views
from .views import InfoPageDetailView

urlpatterns = [
    path('infopage/<slug:slug>/', InfoPageDetailView.as_view(), name='infopage'),
    # /main/infopage/politika-konfidencialnosti/
    path('about/', views.about, name='about'),
    path('fag/', views.fag, name='fag'),
    path('feedback/', views.feedback, name='feedback'),
    path('chat/', views.chat, name='chat'),
]
