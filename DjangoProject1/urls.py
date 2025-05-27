"""
URL configuration for DjangoProject1 project.
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import home, register, user_login  # Импорт из main/views.py вместо frontend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks/', include('tasks.urls')),

    # Убрал frontend.urls, так как все маршруты теперь в main.urls
    path('', include('tasks.urls')),  # Все основные маршруты из main/urls.py

    # Оставил прямые ссылки для совместимости (можно убрать, если они есть в main.urls)
    path('login/', user_login, name='login'),  # Используем user_login из main/views
    path('register/', register, name='register'),
]