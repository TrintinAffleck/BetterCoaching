from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE, unique=True)
    name = models.CharField(max_length = 100, blank = True, null = True)
    email = models.CharField(max_length = 100, blank = True, null = True)
    is_coach = models.BooleanField()
    if is_coach == True:
        profile_img = models.ImageField(null = True, blank = True, upload_to = 'profiles/', default = 'profiles/user-default.png')
        summoner_link = models.CharField(max_length = 250, blank = True, null = True)
    discord_link = models.CharField(max_length = 50, null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                          primary_key = True, editable = False)

    def __str__(self):
        return str(self.name)