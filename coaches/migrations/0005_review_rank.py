# Generated by Django 4.1.1 on 2022-10-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0004_remove_coach_rank_rank_coach_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rank',
            field=models.ManyToManyField(blank=True, to='coaches.rank'),
        ),
    ]