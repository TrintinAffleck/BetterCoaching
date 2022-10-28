from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('coaches.urls'),name='coaches')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(f"YOUR PATH = {settings.MEDIA_URL}")