# Generated by Django 3.2.9 on 2021-12-09 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Workout', '0005_auto_20211208_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='goaltracker',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
