from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.getRoutes),
    path('coaches', views.getCoaches),
    path('coach/<str:pk>', views.getCoach),
    path('coach/<str:pk>/vote', views.coachReview),
    path('users/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]