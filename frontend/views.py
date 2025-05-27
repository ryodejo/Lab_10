from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, "Front.html")  # ✅ Просто загружает страницу без данных

# Страница входа
def login_page(request):
    return render(request, "login.html")  # ✅ Загружает шаблон логина

# Страница регистрации
def register_page(request):
    return render(request, "register.html")  # ✅ Загружает шаблон регистрации

# Страница списка тестов (данные загружаются в `tasks/views.py`)
def test_list_page(request):
    return render(request, "test_list.html")  # ✅ Просто рендерит шаблон")