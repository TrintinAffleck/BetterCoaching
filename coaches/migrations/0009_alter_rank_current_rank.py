# Generated by Django 4.1.1 on 2022-10-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0008_remove_rank_coach_remove_review_rank_coach_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='current_rank',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond'), ('Master', 'Master Tier'), ('GM', 'Grandmaster'), ('Chall', 'Challenger')], default='UNRANKED', max_length=100),
        ),
    ]
