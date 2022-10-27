from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from workshop_petstagram.common.models import Like
from workshop_petstagram.photos.models import Photo


def index(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, template_name='home-page.html', context=context,)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()
    
    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()
        
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url("photo details", photo_id))

    return redirect(request.META["HTTP_REFERER"] + f'#{photo_id}')
