# Generated by Django 4.1.1 on 2022-12-26 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created_date']},
        ),
    ]
