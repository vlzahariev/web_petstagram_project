from django.db import models

from workshop_petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    MAX_COMMENT_TEXT_LENGTH = 300
    comment_text = models.TextField(
        max_length=MAX_COMMENT_TEXT_LENGTH,
        blank=False
    )

    date_time_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
    # when we have users
    # to_user = models.ForeignKey(
    #     User
    # )