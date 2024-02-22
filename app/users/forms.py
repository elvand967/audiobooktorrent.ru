# D:\Python\myProject\audiobooktorrent.ru\app\users\forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

''' Форма регистрации нового пользователя '''
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254,
                             help_text='Обязательное поле. Введите действующий адрес электронной почты.')
    first_name = forms.CharField(max_length=30, required=True, help_text='Обязательное поле. Введите ваше имя.',
                                 label="Имя (Имя Отчество)")
    familiarized = forms.BooleanField(required=False, label="я ознакомлен(а) с")
    # required=False, - допускаем пустое значение (False), для дальнейшей проверки пользовательского валидатора

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2', 'familiarized']

    def clean_familiarized(self):
        familiarized = self.cleaned_data['familiarized']
        if familiarized == False:
            raise ValidationError('Пожалуйста, ознакомьтесь с политикой конфиденциальности и пользовательским соглашением и установите соответствующую отметку в чек-боксе.')
        return familiarized


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=254,
#                              help_text='Обязательное поле. Введите действующий адрес электронной почты.')
#     first_name = forms.CharField(max_length=30, required=True, help_text='Обязательное поле. Введите ваше имя.',
#                                  label="Имя (Имя Отчество)")
#     familiarized = forms.BooleanField(required=False,  label="я ознакомлен(а) с")
#     # required=False, - допускаем пустое значение (False), для дальнейшей проверки пользовательского валидатора
#     def clean_familiarized(self):
#         familiarized = self.cleaned_data.get('familiarized')
#         if not familiarized:
#             raise forms.ValidationError(
#                 "Пожалуйста, для успешного завершения регистрации ознакомьтесь с Политикой конфиденциальности "
#                 "и Пользовательским соглашением и сделайте соответствующую отметку в чек-боксе.")
#         return familiarized
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'email', 'password1', 'password2', 'familiarized']








''' Форма входа пользователя '''
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class ProfileForm(UserChangeForm):
    username = forms.CharField(label="Nik")
    email = forms.EmailField(label="Email / Login", widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
