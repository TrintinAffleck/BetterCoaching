from django.urls import path
from . import views

urlpatterns = [
    # path('',views.editUserAccount,name='users'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.editUserAccount, name='account'),
    path('inbox/', views.inbox,name='inbox'),
    path('inbox/message/<str:pk>/', views.viewMessage, name='message'),
    path('inbox/send-message/<str:pk>', views.sendMessage, name='send-message'),
]