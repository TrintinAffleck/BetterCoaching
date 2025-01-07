from django.contrib import admin
from .models import Review, Coach, Accomplishments
# Register your models here.

admin.site.register(Review)
admin.site.register(Coach)
admin.site.register(Accomplishments)
