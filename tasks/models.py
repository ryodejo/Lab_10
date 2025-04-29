from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=255)  # Название теста
    description = models.TextField(blank=True, null=True)  # Описание теста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.title

class Topic(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="topics")  # Связь с тестами
    title = models.CharField(max_length=255)  # Название темы

    def __str__(self):
        return self.title

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")  # Связь с темой
    text = models.TextField()  # Текст вопроса

    def __str__(self):
        return self.text