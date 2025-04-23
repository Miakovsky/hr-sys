from django.contrib import admin
from .models import *
from django.core.mail import send_mail

admin.site.site_header = 'HR-система'
admin.site.site_title = 'HR-система'

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'check_citizenship']
    list_filter = ['created']
    search_fields = ['education_level', 'education_details', 'work_experience', 'skills', 'additional_info']
    actions = ['invite']

    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name}"
   
    @admin.display(boolean = True, description='Российское гражданство')
    def check_citizenship(self, obj):
        if obj.citizenship.lower() in ('россия', 'российское', 'россиянин','россиянка'):
            return True
        else: return False

    @admin.action(description='Пригласить на интервью')
    def invite(modelAdmin, request, queryset):
        for person in queryset:
            send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            [f"{person.email}"],
            fail_silently=False,
        )
        modelAdmin.message_user(
            request, 'Кандидаты были приглашены на интервью.'
        )
admin.site.register(Application, ApplicationAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', ('min_age', 'max_age'), 'min_education', 'keywords']
admin.site.register(Job, JobAdmin)

