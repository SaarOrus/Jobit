from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='users-profile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    #path('profile/<str:username>/', views.profile, name='users-profile'),
]
