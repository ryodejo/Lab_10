from django.contrib import admin
from .models import Test, Topic, Question, Answer

from django.contrib import admin
from .models import Test, Topic, Question, Answer

class TopicInline(admin.TabularInline):  # Темы внутри теста
    model = Topic
    extra = 1

class QuestionInline(admin.TabularInline):  # Вопросы внутри темы
    model = Question
    extra = 1

class AnswerInline(admin.TabularInline):  # Ответы внутри вопроса
    model = Answer
    extra = 3  # Показывать 3 пустых поля для добавления ответов

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [TopicInline]  # Добавляем темы внутрь теста

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "test")
    inlines = [QuestionInline]  # Добавляем вопросы внутрь темы

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "topic")
    inlines = [AnswerInline]  # Добавляем ответы внутри вопросов

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct", "question__topic")  # Фильтр по теме