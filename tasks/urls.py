from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path("register/", register, name="register"),  # Регистрация
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),  # Вход
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),  # Выход
]