# Generated by Django 4.1.1 on 2022-11-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0022_alter_coach_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='profile_img',
            field=models.ImageField(default='images/BG_logo.JPG', null=True, upload_to=''),
        ),
    ]
