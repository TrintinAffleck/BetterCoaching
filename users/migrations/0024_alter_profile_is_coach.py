# Generated by Django 4.1.7 on 2023-04-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0023_alter_message_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="is_coach",
            field=models.BooleanField(default=False),
        ),
    ]