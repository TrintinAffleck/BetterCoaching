from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('coaches.urls'), name='coaches'),
    path('users/', include('users.urls'), name='users'),
    path('api/', include('api.urls'), name='api'),

    path('reset-password', auth_views.PasswordResetView.as_view(template_name="users/reset-password.html"),
         name="reset_password"),

    path('reset-password_sent', auth_views.PasswordResetDoneView.as_view(template_name="users/reset-password-done.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]


#Static URLS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
