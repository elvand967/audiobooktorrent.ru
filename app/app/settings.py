# D:\Python\myProject\audiobooktorrent.ru\app\app\settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Создайте пути внутри проекта следующим образом: BASE_DIR/'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: храните секретный ключ, используемый в производстве, в тайне!
SECRET_KEY = 'django-insecure-k_-poamx=!^40)wg2pey%wsf8v6$1yr+3qi(j&-7p(tarv0-c%'

# SECURITY WARNING: don't run with debug turned on in production!
# ПРЕДУПРЕЖДЕНИЕ БЕЗОПАСНОСТИ: не запускайте с включенной отладкой в рабочей среде!
DEBUG = True

ALLOWED_HOSTS = ['*', '127.0.0.1']


# Application definition
# Определение приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main.apps.MainConfig',
    'audiobooks.apps.AudiobooksConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'vdubanbu_db_abt',
    #     'USER': 'vdubanbu_db_abt',
    #     'PASSWORD': 'MoloVG12432*',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    # },
    'database_books': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "D:/Python/myProject/BazaKnig_parser_db/database_books.db",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# Интернационализация
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_ROOT – путь к общей статической папке, формируемой при запуске команды collectstatic
# (для сбора всей статики в единый каталог при размещении сайта на реальном веб-сервере);
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATIC_URL – префикс URL-адреса для статических файлов;
STATIC_URL = 'static/'

# STATICFILES_DIRS – список дополнительных (нестандартных) путей к статическим файлам,
# используемых для сбора и для режима отладки.
# STATICFILES_DIRS = [BASE_DIR / 'static',]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Выход пользователя с переадресацией на корневую страницу
LOGOUT_REDIRECT_URL = '/'
