from django.urls import path
from . import views
from .views import register, start_test, result
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("start_test/", start_test, name="start_test"),
    path('result/', views.result, name='result')
]