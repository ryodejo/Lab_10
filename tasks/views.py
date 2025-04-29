from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms_regis import RegisterForm
from .models import Test, Question, Answer, TestResult
from django.contrib.auth.decorators import login_required

def home(request):
    return HttpResponse("Добро пожаловать в Django!")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

@login_required  # Требуется авторизация
def start_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(topic__test=test)
    return render(request, "tests/start_test.html", {"test": test, "questions": questions})

@login_required
def submit_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(topic__test=test)

    score = 0  # Подсчёт правильных ответов

    for question in questions:
        user_answer = request.POST.get(f"question_{question.id}")  # Получаем ответ пользователя
        correct_answer = Answer.objects.filter(question=question, is_correct=True).first()

        if correct_answer and user_answer == correct_answer.text:
            score += 1  # Начисляем баллы за правильный ответ

    # Сохранение результата в базе
    TestResult.objects.create(user=request.user, test=test, score=score)

    return render(request, "tests/result.html", {"test": test, "score": score})