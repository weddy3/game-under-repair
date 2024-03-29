# Generated by Django 5.0 on 2024-01-01 21:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_round_post', '0002_golfround_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfround',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='golfround',
            name='score',
            field=models.SmallIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='golfround',
            name='total_strokes_gained',
            field=models.FloatField(default=0.0),
        ),
    ]
