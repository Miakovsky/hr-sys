from django import forms
from .models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['picture', 'last_name', 'first_name', 'patronim', 'phone', 'email',
                  'date_of_birth', 'gender', 'citizenship', 'education_level', 
                  'education_details', 'work_experience', 'skills', 'additional_info']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'patronim': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'phone': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'email': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control border-0'}),
            'education_details': forms.TextInput(attrs={'class': 'form-control border-0', 'textarea rows':"3"}),
            'work_experience': forms.TextInput(attrs={'class': 'form-control border-0', 'textarea rows':"3"}),
            'skills': forms.TextInput(attrs={'class': 'form-control border-0', 'textarea rows':"3"}),
            'additional_info': forms.TextInput(attrs={'class': 'form-control border-0', 'textarea rows':"3"}),
            'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'gender': forms.Select(attrs={'class': 'form-control border-0'}),
            'education_level': forms.Select(attrs={'class': 'form-control border-0'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control border-0'}),
            }