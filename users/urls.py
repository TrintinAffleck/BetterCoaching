from django.urls import path
from . import views

urlpatterns = [
    path('',views.editUserAccount,name='users'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.editUserAccount, name='account'),
]