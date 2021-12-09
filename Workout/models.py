from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    exercise_name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    calories = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)


class GoalTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default=None)
    current_Weight = models.PositiveIntegerField(default=0, blank=True, null=True)
    goal_Weight = models.PositiveIntegerField(default=0, blank=True, null=True)
    one_Mile_Time = models.CharField(max_length=200, default="0:00")
    bench_Press_Reps = models.PositiveIntegerField(default=0, blank=True, null=True)
    bench_Press_Weight = models.PositiveIntegerField(default=0, blank=True, null=True)
    squat_Reps = models.PositiveIntegerField(default=0, blank=True, null=True)
    squat_Weight = models.PositiveIntegerField(default=0, blank=True, null=True)
    deadlift_Reps = models.PositiveIntegerField(default=0, blank=True, null=True)
    deadlift_Weight = models.PositiveIntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)



