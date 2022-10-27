from django.shortcuts import render, redirect

from workshop_petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from workshop_petstagram.pets.models import Pet


# Create your views here.


def details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, template_name='pet-details-page.html', context=context)


def add(request):
    form = PetCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile details', pk=1)

    context = {
        'form': form
    }
    return render(request, template_name='pet-add-page.html', context=context)


def edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "GET":
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets details', username, pet_slug)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username,
    }
    return render(request, template_name='pet-edit-page.html', context=context)


def delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == "POST":
        pet.delete()
        return redirect('profile details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        'form': form
    }
    return render(request, 'pet-delete-page.html', context)
