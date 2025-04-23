from django import forms
from .models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['picture', 'last_name', 'first_name', 'patronim', 'phone', 'email',
                  'date_of_birth', 'gender', 'citizenship', 'education_level', 
                  'education_details', 'work_experience', 'skills', 'additional_info']
        widgets = {
            'date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            }