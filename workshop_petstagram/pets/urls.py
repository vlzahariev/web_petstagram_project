from django.urls import path, include

from workshop_petstagram.pets import views

urlpatterns = (
    path('pets/', views.add, name="pets add"),
    path('pets/<str:username>/pet/<slug:pet_name>/', include([
        path('edit/', views.edit, name='pets edit'),
        path('delete/', views.delete, name='pets delete'),
        path('', views.details, name='pets details'),
    ]))
)
