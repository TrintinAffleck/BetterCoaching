# Generated by Django 4.1.1 on 2022-11-16 20:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0037_alter_coach_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
