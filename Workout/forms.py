from django import forms
from .models import Exercise, GoalTracker


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'


class GoalForm(forms.ModelForm):
    class Meta:
        model = GoalTracker
        fields = '__all__'
