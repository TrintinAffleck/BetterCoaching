from django.db import models
import uuid
from users.models import Profile

class Coach(models.Model):
    user = models.ForeignKey(
        Profile, null = True, blank = True, on_delete = models.CASCADE
    )
    display_name = models.CharField(max_length = 250)
    headline = models.CharField(max_length = 60, null = True, blank = True)
    body = models.TextField(max_length = 10000, null = True, blank = True)
    rating_total = models.IntegerField(default = 0, null = True, blank = True)
    rating_ratio = models.IntegerField(default = 0, null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(
        default = uuid.uuid4, unique = False, primary_key = True, editable = False
    )
    discord_link = models.CharField(max_length = 60, null = True)
    profile_img = models.ImageField(null = True, default = "BG_logo.JPG")

    @property
    def reviewers(self):
        return self.review_set.all().values_list('owner__id',flat=True)

    @property
    def get_votes(self):
        reviews = self.review_set.all()
        total = reviews.count()
        if total > 0:
            rating_sum = 0
            for review in reviews:
                # rating_sum += float(review.rating_value)
                print(type(review.rating_value))
            average_rating = rating_sum / total
        else:
            average_rating = 0
        self.rating_total = total
        self.rating_ratio = average_rating
        self.save()


    class Meta():
        ordering = ['-rating_ratio','-rating_total']

    def __str__(self) -> str:
        return self.display_name

class Review(models.Model):
    owner = models.ForeignKey(Profile, on_delete = models.DO_NOTHING) #User who gave the review
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE)  #Coach who received the review.
    VOTE_TYPES = (
        ('5.0', 5),
        ('4.5', 4.5),
        ('4.0', 4),
        ('3.5', 3.5),
        ('3.0', 3),
        ('2.5', 2.5),
        ('2.0', 2),
        ('1.5', 1.5),
        ('0.0', 1),
        ('0.5', 0.5),
        ('0', 0)
    )
    body = models.TextField(null = True, blank = True)
    rating_value = models.SmallIntegerField(choices = VOTE_TYPES)
    created_date = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(
        default = uuid.uuid4, unique = True, primary_key = True, editable = False
    )

    class Meta():
        ordering = ['-created_date']

    def __str__(self) -> str:
        return str(f"{self.owner}" + " | " + f"{self.rating_value}")

class Accomplishments(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    owner = models.ForeignKey(Coach, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return str(f"{self.owner}" + " | " + f"{self.name}")
