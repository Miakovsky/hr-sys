from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import *

def main(request):
    form = ApplicationForm()
    return render(request, 'main.html', {'form': form})

def application_form(request):
    form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form})

def form_create(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('success')
        else:
            print(form.errors.as_data())
            return render(request, 'application_form.html', {'form': form})
    else:
        form = ApplicationForm()
        return render(request, 'application_form.html', {'form': form})
    
def success(request):
    return render(request, 'success.html')
