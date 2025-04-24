from django.contrib import admin
from .models import *
from django.core.mail import send_mail
import string
from datetime import date

admin.site.site_header = 'HR-система'
admin.site.site_title = 'HR-система'

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'check_citizenship', 'check_age', 'compat_check']
    list_filter = ['created']
    search_fields = ['education_level', 'education_details', 'work_experience', 'skills', 'additional_info']
    actions = ['invite']

    @admin.display(description='Кандидат')
    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"
   
    @admin.display(boolean = True, description='Российское гражданство')
    def check_citizenship(self, obj):
        if obj.citizenship.lower() in ('россия', 'российское', 'россиянин','россиянка', 'рф'):
            return True
        else: return False

    @admin.display(boolean = True, description='Подходящий возраст')
    def check_age(self, obj):
        age = self.get_age(obj)
        for item in Job.objects.all():
            if age < item.min_age or age > item.max_age:
                return False
            else: return True

    @admin.action(description='Пригласить на собеседование')
    def invite(modelAdmin, request, queryset):
        for person in queryset:
            send_mail(
            f"Пришлашение на собеседование",
            f"Добрый день, {person.first_name} {person.patronim}. Мы приглашаем вас на собеседование в компанию GAMING.\nПросим вас прийти а наш офис по адресу Улица Бабушкина, 34, кабинет 3 в 12:00.\nВсего наилучшего, GAMING.",
            "GAMING@example.com",
            [f"{person.email}"],
            fail_silently=False,
        )
        modelAdmin.message_user(
            request, 'Выбраные кандидаты были приглашены на собеседование!'
        )
    def get_age(self, obj):
            dob = obj.date_of_birth

            today = date.today()
            age = int(today.year) - int(dob.year) - ((int(today.month), int(today.day)) < (int(dob.month), int(dob.day)))
            return age 

    @admin.display(description='Баллы')
    def compat_check(self, obj):
        edu_level = ['Среднее',
        'Среднее профессиональное',
        'Бакалавриат',
        'Магистратура',]
    
        score = {}
        relevant = [word.strip(string.punctuation) for word in obj.skills.split()]
        relevant += [word.strip(string.punctuation) for word in obj.education_details.split()]
        relevant += [word.strip(string.punctuation) for word in obj.additional_info.split()]
        relevant_experience = [word.strip(string.punctuation) for word in obj.work_experience.split()]
        for item in Job.objects.all():
            score[item.title] = 0
            keywords = [word.strip(string.punctuation) for word in item.keywords.split()]
            for word in keywords:
                if word in relevant:
                    score[item.title] += 1
                if word in relevant_experience:
                    score[item.title] += 5
            if edu_level.index(item.min_education) <= edu_level.index(obj.education_level):
                score[item.title] *= 2
        final_score = "<br>".join(f"{k}: {v}" for k, v in score.items())
        return mark_safe(final_score)

      

admin.site.register(Application, ApplicationAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', ('min_age', 'max_age'), 'min_education', 'keywords']
admin.site.register(Job, JobAdmin)


