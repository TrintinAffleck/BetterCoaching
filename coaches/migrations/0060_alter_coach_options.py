# Generated by Django 4.1.1 on 2023-01-21 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0059_alter_review_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'ordering': ['rating_ratio', 'rating_total']},
        ),
    ]
