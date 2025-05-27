from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms_regis import RegisterForm
from .models import Test, Topic, Question, Answer, TestResult
from django.contrib.auth.models import User


def home(request):
    """Главная страница"""
    return render(request, "Front.html")


def register(request):
    """Регистрация нового пользователя"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация успешна! Добро пожаловать!")
            return redirect("test_list")
        messages.error(request, "Ошибка регистрации. Проверьте данные.")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    """Авторизация пользователя"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next") or "/tests/"

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли!")
            return HttpResponseRedirect(next_url)
        messages.error(request, "Неверное имя пользователя или пароль.")

    next_url = request.GET.get("next", "")
    return render(request, "login.html", {"next": next_url})


@login_required
def user_logout(request):
    """Выход из системы"""
    logout(request)
    messages.success(request, "Вы вышли из аккаунта.")
    return redirect("home")


@login_required
def test_list(request):
    """Список всех тестов сгруппированных по темам"""
    tests = Test.objects.all().prefetch_related('topics')
    return render(request, "test_list.html", {"tests": tests})


@login_required
def topic_tests(request, topic_id):
    """Тесты конкретной темы"""
    topic = get_object_or_404(Topic, id=topic_id)
    tests = Test.objects.filter(topics=topic)
    return render(request, "topic_tests.html", {
        "topic": topic,
        "tests": tests
    })


@login_required
def start_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    # Получаем все вопросы, связанные с тестом через темы
    questions = Question.objects.filter(topic__test=test).prefetch_related('answers')
    return render(request, "start_test.html", {
        "test": test,
        "questions": questions,
    })


@login_required
def submit_test(request, test_id):
    """Обработка результатов теста"""
    test = get_object_or_404(Test, id=test_id)
    # Получаем все вопросы, связанные с тестом через темы
    questions = Question.objects.filter(topic__test=test).prefetch_related('answers')
    score = 0
    total_questions = questions.count()

    for question in questions:
        # Получаем правильный ответ (один)
        correct_answer = question.answers.filter(is_correct=True).first()
        # Получаем ID выбранного ответа из POST (строка)
        selected_answer_id = request.POST.get(f"question_{question.id}")

        # Проверяем, что выбранный ответ есть и совпадает с правильным
        if selected_answer_id and correct_answer:
            try:
                if int(selected_answer_id) == correct_answer.id:
                    score += 1
            except ValueError:
                # В случае, если selected_answer_id не число, пропускаем
                pass

    # Сохраняем результат теста
    TestResult.objects.create(
        user=request.user,
        test=test,
        score=score
    )

    messages.success(request, f"Тест завершён! Результат: {score}/{total_questions}")
    return redirect("result", test_id=test.id)



@login_required
def result(request, test_id):
    """Просмотр результатов теста"""
    test = get_object_or_404(Test, id=test_id)
    test_result = TestResult.objects.filter(
        user=request.user,
        test=test
    ).order_by('-completed_at').first()

    if not test_result:
        messages.error(request, "Результаты теста не найдены.")
        return redirect('test_list')

    return render(request, "result.html", {
        "test": test,
        "test_result": test_result
    })



def contact(request):
    """Страница контактов"""
    return render(request, "contact.html")


def about(request):
    """Страница 'О нас'"""
    return render(request, "about.html")
