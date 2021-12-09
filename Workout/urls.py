from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.index, name="index"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('register', views.register, name="register"),
    path('workouts', views.render_workouts, name="workouts"),
    path('create', views.create_workout, name="create"),
    path('delete/<int:workout_id>', views.delete_workout, name="delete"),
    path('update/<int:workout_id>', views.update_workout, name="update"),
    path('goals', views.render_goals, name="goals"),
    path('updateGoals/<int:goal_id>', views.update_goals, name="updateGoals"),
    path('createGoals', views.create_goals, name="createGoals"),
    path('deleteGoals/<int:goal_id>', views.delete_goals, name="deleteGoals")
]