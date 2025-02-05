# Generated by Django 4.1.7 on 2023-04-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coaches", "0062_rename_user_type_coach_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating_value",
            field=models.SmallIntegerField(
                choices=[
                    ("5.0", "5"),
                    ("4.5", "4.5"),
                    ("4.0", "4.0"),
                    ("3.5", "3.5"),
                    ("3.0", "3.0"),
                    ("2.5", "2.5"),
                    ("2.0", "2.0"),
                    ("1.5", "1.5"),
                    ("0.0", "1.0"),
                    ("0.5", "0.5"),
                    ("0", "0"),
                ]
            ),
        ),
    ]
