# Generated by Django 4.1.1 on 2022-11-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0033_alter_coach_rank_alter_rank_current_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
