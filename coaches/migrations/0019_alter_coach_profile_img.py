# Generated by Django 4.1.1 on 2022-11-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0018_alter_coach_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='profile_img',
            field=models.ImageField(default='C:\\Users\\taffl\\Desktop\\Programming\\BetterCoaching\\static\\images\\BG_logo.jpg', null=True, upload_to=''),
        ),
    ]
