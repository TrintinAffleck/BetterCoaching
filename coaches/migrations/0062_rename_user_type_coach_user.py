# Generated by Django 4.1.7 on 2023-04-21 03:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("coaches", "0061_alter_coach_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="coach",
            old_name="user_type",
            new_name="user",
        ),
    ]