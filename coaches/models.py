from django.db import models
import uuid
from users.models import Profile, User


class Coach(models.Model):
    user_type = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE
    )
    display_name = models.CharField(max_length=250)
    headline = models.CharField(max_length=60, null=True, blank=True)
    body = models.TextField(max_length=5000, null=True, blank=True)
    rating_total = models.IntegerField(default=0, null=True, blank=True)
    rating_ratio = models.IntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    discord_link = models.CharField(max_length=60, null=True)
    profile_img = models.ImageField(null=True, default="BG_logo.JPG")

    def __str__(self) -> str:
        return self.display_name


class Review(models.Model):
    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE
    )  # Many to One Relationship
    VOTE_TYPES = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )
    body = models.TextField(null=True, blank=True)
    rating_value = models.CharField(max_length=200, choices=VOTE_TYPES)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.rating_value


class Accomplishments(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(f"{self.owner}" + " | " + f"{self.name}")
