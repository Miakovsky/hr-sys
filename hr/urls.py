from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('apply/', views.application_form, name='application_form'),
    path('apply/create', views.form_create, name='form_create'),
    path('success', views.success, name='success'),
]