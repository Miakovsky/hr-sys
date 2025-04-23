from django.contrib import admin
from .models import *
from django.core.mail import send_mail
import string

admin.site.site_header = 'HR-система'
admin.site.site_title = 'HR-система'

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'check_citizenship', 'compat_check']
    list_filter = ['created']
    search_fields = ['education_level', 'education_details', 'work_experience', 'skills', 'additional_info']
    actions = ['invite']

    @admin.display(description='Кандидат')
    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"
   
    @admin.display(boolean = True, description='Российское гражданство')
    def check_citizenship(self, obj):
        if obj.citizenship.lower() in ('россия', 'российское', 'россиянин','россиянка'):
            return True
        else: return False

    @admin.action(description='Пригласить на собеседование')
    def invite(modelAdmin, request, queryset):
        for person in queryset:
            send_mail(
            f"Пришлашение на собеседование",
            f"Добрый день, {person.first_name} {person.patronim}. Мы приглашаем вас на собеседование.",
            "from@example.com",
            [f"{person.email}"],
            fail_silently=False,
        )
        modelAdmin.message_user(
            request, 'Выбраные кандидаты были приглашены на интервью.'
        )

    @admin.display(description='Баллы')
    def compat_check(self, obj):
        edu_level = ['Среднее',
        'Среднее профессиональное',
        'Бакалавриат',
        'Магистратура',]
    
        score = {}
        for item in Job.objects.all():
            score[item.title] = 0
            keywords = [word.strip(string.punctuation) for word in item.keywords.split()]
            for word in keywords:
                if word in (obj.skills, obj.work_experience, 
                            obj.education_details, obj.additional_info):
                    score[item.title] += 1
            if edu_level.index(item.min_education) <= edu_level.index(obj.education_level):
                score[item.title] += 5
                print(item.min_education)
        final_score = "\n".join(f"{k}: {v}" for k, v in score.items())
        return final_score

        

admin.site.register(Application, ApplicationAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', ('min_age', 'max_age'), 'min_education', 'keywords']
admin.site.register(Job, JobAdmin)


