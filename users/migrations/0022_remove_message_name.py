# Generated by Django 4.1.1 on 2023-02-01 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_profile_email_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
    ]