from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.profiles,name='profiles'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.userAccount, name='account')
]