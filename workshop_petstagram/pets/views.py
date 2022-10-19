from django.shortcuts import render

# Create your views here.


def add(request):
    return render(request, template_name='pet-add-page.html')


def edit(request, username, pet_name):
    return render(request, template_name='pet-edit-page.html')


def delete(request, username, pet_name):
    return render(request, template_name='pet-delete-page.html')


def details(request, username, pet_name):
    return render(request, template_name='pet-details-page.html')