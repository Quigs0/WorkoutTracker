from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import WorkoutForm, GoalForm
from .models import Exercise, GoalTracker

# Create your views here.


def index(request):
    return render(request, 'homepage.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
def create_workout(request):
    form = WorkoutForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('workouts')

    return render(request, 'create.html', {'form': form})


@login_required(login_url='login')
def render_workouts(request):
    my_workouts = Exercise.objects.filter(user=request.user)
    context = {'my_workouts': my_workouts}
    return render(request, 'workouts.html', context)

@login_required(login_url='login')
def delete_workout(request, workout_id):
    my_workouts = Exercise.objects.get(id=workout_id)

    if request.method == 'POST':
        my_workouts.delete()
        return redirect('workouts')

    return render(request, 'delete.html', {'my_workouts': my_workouts})

@login_required(login_url='login')
def update_workout(request, workout_id):
    my_workouts = Exercise.objects.get(id=workout_id)

    form = WorkoutForm(request.POST or None, instance=my_workouts)

    if form.is_valid():
        form.save()
        return redirect('workouts')

    context = {'form': form, 'workout_id': workout_id}
    return render(request, 'update.html', context)


@login_required(login_url='login')
def render_goals(request):
    my_goals = GoalTracker.objects.filter(user=request.user)
    context = {'my_goals': my_goals}
    return render(request, 'goals.html', context)


@login_required(login_url='login')
def create_goals(request):
    form = GoalForm(request.POST or None)

    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('goals')

    return render(request, 'createGoals.html', {'form': form})


@login_required(login_url='login')
def update_goals(request, goal_id):
    my_workouts = GoalTracker.objects.get(id=goal_id)

    form = GoalForm(request.POST or None, instance=my_workouts)

    if form.is_valid():
        form.save()
        return redirect('goals')

    context = {'form': form}
    return render(request, 'updateGoal.html', context)

@login_required(login_url='login')
def delete_goals(request, goal_id):
    my_goals = GoalTracker.objects.get(id=goal_id)

    if request.method == 'POST':
        my_goals.delete()
        return redirect('goals')

    return render(request, 'deleteGoals.html', {'my_goals': my_goals})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
