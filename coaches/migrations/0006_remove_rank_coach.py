# Generated by Django 4.1.1 on 2022-10-16 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0005_review_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rank',
            name='coach',
        ),
    ]