# Generated by Django 4.1.1 on 2023-01-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0051_alter_coach_id_alter_review_rating_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='body',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]