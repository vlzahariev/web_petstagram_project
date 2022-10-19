from django.urls import path, include

from workshop_petstagram.accounts.views import profile_edit, profile_register, profile_login, profile_delete, \
    profile_details
urlpatterns = (
    path('register/', profile_register, name='register'),
    path('login/', profile_login, name='login'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name="profile details"),
        path('edit/', profile_edit, name="profile edit"),
        path('delete/', profile_delete, name="profile delete"),
    ]))
)
