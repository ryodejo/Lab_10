from pathlib import Path

# Определение базового пути проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (НЕ раскрывать!)
SECRET_KEY = 'django-insecure-z5@9jjds$^je5&nm_mw40ew3tm_(#i=96s=j&2l3$k2#l0xy)='

# Включение режима отладки (выключить в продакшене!)
DEBUG = True

# Разрешенные хосты (указать домены в продакшене)
ALLOWED_HOSTS = []

# Установленные приложения
INSTALLED_APPS = [
    'tasks',
    'frontend',
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
        'DIRS': [BASE_DIR / 'frontend/templates'],  # ✅ Путь к шаблонам
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
        'ENGINE': 'django.db.backends.sqlite3',
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
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Настройки статических файлов (CSS, JS, изображения)
# settings.py (оставляем как есть)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "frontend/static"]  # Путь к вашей статике
STATIC_ROOT = BASE_DIR / "staticfiles"
# Настройки медиа-файлов (изображения, документы)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Автоматическое определение типа первичного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки авторизации
LOGIN_REDIRECT_URL = "/Maths/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "/login/"