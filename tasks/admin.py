from django.contrib import admin
from .models import Test, Topic

class TopicInline(admin.TabularInline):  # Позволяет добавлять темы прямо при редактировании теста
    model = Topic
    extra = 1  # Количество пустых полей для добавления новых тем

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title",)
    inlines = [TopicInline]  # Включаем редактирование тем внутри теста

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "test")  # Показываем название темы и тест