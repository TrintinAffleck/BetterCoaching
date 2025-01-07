from django.db import models
import uuid
from users.models import Profile


class Coach(models.Model):
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=250)
    headline = models.CharField(max_length=60, null=True, blank=True)
    body = models.TextField(max_length=10000, null=True, blank=True)
    rating_total = models.IntegerField(default=0, null=True, blank=True)
    rating_ratio = models.IntegerField(default=0, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=False, primary_key=True, editable=False
    )
    discord_link = models.CharField(max_length=60, null=True)
    profile_img = models.ImageField(null=True, default="BG_logo.JPG")

    @property
    def reviewers(self):
        return self.review_set.all().values_list("id", flat=True)

    @property
    def get_average(self):
        """Gets the average rating of the coach reviews"""
        reviews = self.review_set.all()
        total = len(self.reviewers)
        if total > 0:
            # Calculate the sum of all ratings, excluding the deleted reviews
            rating_sum = sum(
                review.rating_value for review in reviews if not review.deleted
            )
            # Calculate the new average rating
            average_rating = rating_sum / len(
                [review for review in reviews if not review.deleted]
            )
        else:
            average_rating = 0
        self.rating_total = total
        self.rating_ratio = average_rating
        self.save()
        return average_rating

    def delete(self, using=None, keep_parents=False):
        """Gets all the related reviews and deletes them"""
        reviews = self.review_set.all()
        for review in reviews:
            review.delete(is_cascade_delete=True)
        super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        ordering = ["-rating_ratio", "-rating_total"]

    def __str__(self) -> str:
        return self.display_name


class Review(models.Model):
    owner = models.ForeignKey(
        Profile,
        default="deleted-user",  # User who gave the review
        on_delete=models.SET_DEFAULT,
    )
    coach = models.ForeignKey(
        Coach, on_delete=models.CASCADE
    )  # Coach who received the review.
    VOTE_TYPES = (
        (5.0, "5.0"),
        (4.5, "4.5"),
        (4.0, "4.0"),
        (3.5, "3.5"),
        (3.0, "3.0"),
        (2.5, "2.5"),
        (2.0, "2.0"),
        (1.5, "1.5"),
        (1.0, "1.0"),
        (0.5, "0.5"),
        (0.0, "0.0"),
    )
    body = models.TextField(null=True, blank=True)
    rating_value = models.FloatField(choices=VOTE_TYPES)
    deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def update_reviewers(self):
        review = Review.objects.get(id=self.id)  # get the review object
        # remove the review from the reviewers list
        new_reviews = self.coach.remove_review_from_reviewers(review)
        self.coach.review_set.set(new_reviews)
        self.coach.save()
        return self.coach.reviewers

    def update_rating_total(self):
        coach = Coach.objects.get(id=self.coach.id)
        coach.rating_total -= 1
        coach.save()

    def update_rating_ratio(self):
        coach = Coach.objects.get(id=self.coach.id)
        coach.rating_ratio = self.coach.get_average
        coach.save()

    def delete(self, using=None, keep_parents=False, is_cascade_delete=False):
        # If this delete is a cascading delete, proceed as usual
        if is_cascade_delete:
            super().delete(using=using, keep_parents=keep_parents)
            return

        # Otherwise, delete the review object without cascading
        self.update_reviewers()
        self.update_rating_total()
        self.update_rating_ratio()
        super().delete(using=using, keep_parents=keep_parents)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self) -> str:
        return str(f"{self.owner}" + " | " + f"{self.rating_value}")


class Accomplishments(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(Coach, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(f"{self.owner}" + " | " + f"{self.name}")
