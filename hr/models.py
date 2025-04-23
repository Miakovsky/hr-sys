from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils.html import mark_safe

class Application(models.Model):
    gender_choices = {
        'Мужской': 'Мужской',
        'Женский': 'Женский',
        'Другой': 'Другой',
    }
    edu_level_choices = {
        'Среднее': 'Среднее',
        'Среднее профессиональное': 'Среднее профессиональное',
        'Бакалавриат': 'Бакалавриат',
        'Магистратура': 'Магистратура',
    }

    picture = models.ImageField(upload_to ='./static/images', verbose_name='Изображение')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    patronim = models.CharField(max_length=200, verbose_name='Отчество')
    phone = models.CharField(max_length = 16, unique = True, verbose_name='Номер телефона')
    email = models.EmailField(max_length=200, db_index=True, unique=True, verbose_name='Электронная почта')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(max_length=100, choices=gender_choices, verbose_name='Пол')
    citizenship = models.CharField(max_length=200, verbose_name='Гражданство')
    education_level = models.CharField(max_length=100, choices=edu_level_choices, verbose_name='Уровень образования')
    education_details  = models.TextField(blank=True, verbose_name='Образование(специальность)')
    work_experience = models.TextField(blank=True, verbose_name='Опыт работы')
    skills = models.TextField(verbose_name='Навыки')
    additional_info = models.TextField(blank=True, verbose_name='Дополнительная информация')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return self.email

class Job(models.Model):
    edu_level_choices = {
        'Среднее': 'Среднее',
        'Среднее профессиональное': 'Среднее профессиональное',
        'Бакалавриат': 'Бакалавриат',
        'Магистратура': 'Магистратура',
    }
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    min_age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(80)], verbose_name='Минимальный возраст')
    max_age = models.PositiveIntegerField(default=80, validators=[MinValueValidator(18), MaxValueValidator(80)], verbose_name='Максимальный возраст')
    min_education = models.CharField(max_length=100, choices=edu_level_choices, verbose_name='Минимальный уровень образования')
    keywords = models.TextField(verbose_name='Ключевые слова (писать через запятую)')


    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title