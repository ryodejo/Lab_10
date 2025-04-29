from django.db import models
from django.contrib.auth.models import User  # Используем стандартную модель пользователей


class Test(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Правильный ли ответ?

    def __str__(self):
        return f"{self.text} ({'Правильный' if self.is_correct else 'Неправильный'})"


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, проходящий тест
    test = models.ForeignKey(Test, on_delete=models.CASCADE)  # Тест, который проходит пользователь
    score = models.IntegerField()  # Количество набранных баллов
    completed_at = models.DateTimeField(auto_now_add=True)  # Дата завершения теста

    def __str__(self):
        return f"{self.user.username} - {self.test.title} ({self.score} баллов)"
