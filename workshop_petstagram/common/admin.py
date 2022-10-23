from django.contrib import admin

from workshop_petstagram.common.models import Comment


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
