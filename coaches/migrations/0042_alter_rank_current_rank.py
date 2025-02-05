# Generated by Django 4.1.1 on 2022-11-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0041_rank_current_division_rank_current_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='current_rank',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond'), ('Master Tier', 'Master Tier'), ('Grandmaster', 'Grandmaster'), ('Challenger', 'Challenger'), ('UNRANKED', 'UNRANKED')], default='UNRANKED', max_length=100),
        ),
    ]
