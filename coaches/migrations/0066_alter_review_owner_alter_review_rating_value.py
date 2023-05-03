# Generated by Django 4.1.7 on 2023-05-03 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0024_alter_profile_is_coach"),
        ("coaches", "0065_alter_review_rating_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="owner",
            field=models.ForeignKey(
                default="deleted-user",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="users.profile",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating_value",
            field=models.FloatField(
                choices=[
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
                ]
            ),
        ),
    ]