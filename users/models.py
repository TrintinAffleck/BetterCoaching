from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from .ranks import RANKS, DIVISIONS

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    rank = models.CharField(max_length=50, choices=RANKS, default='UNRANKED')
    division = models.CharField(max_length=50, choices=DIVISIONS, default='')
    is_coach = models.BooleanField(default=False)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profiles/',
                                    default='profiles/user-default.png')
    discord_link = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta():
        ordering = ['created_date']


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, related_name="messages")
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(max_length=2500)
    is_read = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created_date']
