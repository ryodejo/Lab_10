from django.urls import path
from .views import register  # Импортируем представление регистрации

urlpatterns = [
    path("register/", register, name="register"),  # Маршрут для регистрации
]