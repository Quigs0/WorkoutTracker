# Generated by Django 3.2.9 on 2021-12-09 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Workout', '0004_auto_20211208_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='goaltracker',
            name='bench_Press_Reps',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='bench_Press_Weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='current_Weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='deadlift_Reps',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='deadlift_Weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='goal_Weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='one_Mile_Time',
            field=models.CharField(default='0:00', max_length=200),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='squat_Reps',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='squat_Weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='goaltracker',
            name='user',
            field=models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
