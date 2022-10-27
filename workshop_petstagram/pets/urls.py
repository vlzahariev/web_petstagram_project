from django.urls import path, include

from workshop_petstagram.pets import views

urlpatterns = (
    path('add/', views.add, name="pets add"),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('edit/', views.edit, name='pets edit'),
        path('delete/', views.delete, name='pets delete'),
        path('', views.details, name='pets details'),
    ]))
)
