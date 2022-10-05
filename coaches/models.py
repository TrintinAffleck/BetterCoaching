from django.db import models
import uuid
# Create your models here.

class Coach(models.Model):
    name = models.TextField(max_length = 35, unique=True)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    reviews = models.ManyToManyField('Review')

class Review(models.Model):
    rating = models.IntegerField()
    user_review = models.ForeignKey('Coach', on_delete=models.CASCADE)
    body = models.TextField(max_length = 5000, blank= True)

