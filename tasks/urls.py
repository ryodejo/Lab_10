from django.urls import path
from .views import (
    home,
    register,
    user_login,  # Добавьте этот импорт
    user_logout,  # Добавьте этот импорт
    start_test,
    submit_test,
    result,
    test_list
)

urlpatterns = [
    path("", home, name="home"),  # Главная страница
    path("register/", register, name="register"),  # Регистрация
    path("login/", user_login, name="login"),  # Вход (новый маршрут)
    path("logout/", user_logout, name="user_logout"),  # Выход (новый маршрут)
    path("tests/", test_list, name="test_list"),  # Список тестов
    path("tests/<int:test_id>/", start_test, name="start_test"),  # Запуск теста
    path("tests/<int:test_id>/submit/", submit_test, name="submit_test"),  # Отправка теста
    path('tests/<int:test_id>/result/', result, name='result')
    # Просмотр результата
]