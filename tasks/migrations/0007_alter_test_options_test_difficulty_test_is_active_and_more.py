# Generated by Django 5.2 on 2025-05-21 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_testresult'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['-created_at'], 'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.AddField(
            model_name='test',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Легкий'), ('medium', 'Средний'), ('hard', 'Сложный')], default='medium', max_length=10, verbose_name='Сложность'),
        ),
        migrations.AddField(
            model_name='test',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный тест'),
        ),
        migrations.AddField(
            model_name='test',
            name='time_limit',
            field=models.PositiveIntegerField(default=30, verbose_name='Лимит времени (минуты)'),
        ),
        migrations.AddField(
            model_name='test',
            name='topic',
            field=models.CharField(choices=[('math', 'Математика'), ('history', 'История'), ('it', 'Информационные технологии')], default='math', max_length=10, verbose_name='Тема'),
        ),
        migrations.AddField(
            model_name='test',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='test',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='test',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название теста'),
        ),
    ]
