from django.core.validators import MinLengthValidator
from django.db import models

from workshop_petstagram.pets.models import Pet
from workshop_petstagram.photos.validators import validate_file_size_less_than_5mb


# Create your models here.
class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        validators=(validate_file_size_less_than_5mb,),
    )
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True
    )

    tagged_pets = models.ManyToManyField(Pet, blank=True)

    date_of_publication = models.DateField(
        auto_now=True,
    )
