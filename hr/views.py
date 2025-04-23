from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import *

def main(request):
    context = {}
    return render(request, 'main.html')

def application_form(request):
    form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})

def form_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return render(request, 'success.html', {})
        else:
            print(form.errors.as_data())
            return render(request, 'application_form.html', {'form': form})
    else:
        form = ApplicationForm()
        return render(request, 'application_form.html', {'form': form})
    
def success(request):
    context = {}
    return render(request, 'success.html')
