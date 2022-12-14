from django.urls import path
from . import views

urlpatterns = [
    path('', views.coaches, name='coaches'),
    path('coach/<str:pk>/', views.coach, name = 'coach'),
    path('add-coach/', views.addCoach, name='add-coach'),
    path('update-coach/<str:pk>/', views.updateCoach, name='update-coach'),
    path('delete-coach/<str:pk>/', views.deleteCoach, name='delete-coach')
]