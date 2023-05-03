# Generated by Django 4.1.7 on 2023-04-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coaches", "0063_alter_review_rating_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating_value",
            field=models.IntegerField(
                choices=[
                    ("5.0", 5),
                    ("4.5", 4.5),
                    ("4.0", 4),
                    ("3.5", 3.5),
                    ("3.0", 3),
                    ("2.5", 2.5),
                    ("2.0", 2),
                    ("1.5", 1.5),
                    ("0.0", 1),
                    ("0.5", 0.5),
                    ("0", 0),
                ]
            ),
        ),
    ]