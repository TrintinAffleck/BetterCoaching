from django.db import models
import uuid
# Create your models here.

class Coach(models.Model):
    name = models.CharField(max_length = 250)
    body = models.TextField(max_length =  5000, null = True, blank = True)
    rating_total = models.IntegerField(default = 0, null = True, blank = True)
    rating_ratio = models.IntegerField(default = 0, null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                          primary_key = True, editable = False)
    rank = models.ManyToManyField('Rank',blank = True)
    profile_img = models.ImageField(null = True, default = 'BG_logo.jpg')

    def __str__(self) -> str:
        return self.name

class Review(models.Model):
    #owner =
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE) #Many to One Relationship
    VOTE_TYPES = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    body = models.TextField(null = True, blank = True)
    rating_value = models.CharField(max_length = 200, choices = VOTE_TYPES)
    created_date = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, 
                          primary_key = True, editable = False)
    def __str__(self) -> str:
        return self.rating_value

class Rank(models.Model):
    RANKS = (
        ('Bronze','Bronze'),
        ('Silver','Silver'),
        ('Gold','Gold'),
        ('Platinum','Platinum'),
        ('Diamond','Diamond'),
        ('Master','Master Tier'),
        ('Grandmaster','Grandmaster'),
        ('Challenger','Challenger'),
    )

    DIVISIONS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('',''),
    )
    current_rank = models.CharField(default = 'UNRANKED',max_length = 100, choices = RANKS)
    current_division = models.CharField(default = ' ',max_length = 50, choices = DIVISIONS, blank = True) 

    def __str__(self) -> str:
        return self.current_rank + " " + self.current_division

