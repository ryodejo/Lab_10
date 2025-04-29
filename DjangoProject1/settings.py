"""
Настройки Django для проекта myproject.

Сгенерировано с помощью 'django-admin startproject' на Django 5.2.

Дополнительная информация по настройкам:
https://docs.djangoproject.com/en/5.2/topics/settings/

Полный список настроек:
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Определение базового пути проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Быстрая настройка для разработки (не использовать в продакшене!)
# Подробнее: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# Секретный ключ для приложения (НЕ раскрывать!)
SECRET_KEY = 'django-insecure-z5@9jjds$^je5&nm_mw40ew3tm_(#i=96s=j&2l3$k2#l0xy)='

# Включение режима отладки (выключить в продакшене!)
DEBUG = True

# Разрешенные хосты (указать домены в продакшене)
ALLOWED_HOSTS = []

# Определение установленных приложений
INSTALLED_APPS = [
    'tasks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Промежуточное ПО (middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневой URL-обработчик
ROOT_URLCONF = 'DjangoProject1.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Добавить пути к шаблонам, если требуется
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = 'DjangoProject1.wsgi.application'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Интернационализация
LANGUAGE_CODE = 'ru'  # Установил русский язык по умолчанию
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Настройки статических файлов (CSS, JS, изображения)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Папка для статических файлов (если используется)

# Настройки медиа-файлов (если загружаются изображения или файлы)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Автоматическое определение типа первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки авторизации и перенаправления после входа/выхода
LOGIN_REDIRECT_URL = "/"  # После входа перенаправлять на главную страницу
LOGOUT_REDIRECT_URL = "/"  # После выхода возвращать на главную страницу
LOGIN_URL = "/login/"  # Если пользователь не авторизован, его перенаправят сюда

# Включение настройки AUTHENTICATION_BACKENDS, если требуется кастомная авторизация
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # Стандартная система аутентификации Django
]

# Настройки сессий (срок хранения пользовательских данных в браузере)
SESSION_COOKIE_AGE = 86400  # Время жизни сессии (24 часа)
SESSION_SAVE_EVERY_REQUEST = True  # Продлевать сессию при каждом запросе