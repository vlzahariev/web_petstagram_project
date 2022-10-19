from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def profile_register(request, pk):
    return render(request, template_name='register-page.html')


def profile_login(request, pk):
    return render(request, template_name='login-page.html')


def profile_edit(request, pk):
    return render(request, template_name='profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, template_name='profile-delete-page.html')


def profile_details(request, pk):
    return render(request, template_name='profile-details-page.html')

