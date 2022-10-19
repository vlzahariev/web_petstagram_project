from django.urls import path

from workshop_petstagram.common import views

urlpatterns = (
    path('', views.index, name="index"),
)
