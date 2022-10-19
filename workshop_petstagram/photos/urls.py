from django.urls import path

from workshop_petstagram.photos import views

urlpatterns = (
    path('add/', views.add_photo, name='photo add'),
    path('<int:pk>/', views.details_photo, name='photo details'),
    path('<int:pk>/edit/', views.edit_photo, name='photo edit'),
)
