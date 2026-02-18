from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=140)
    difficulty = models.CharField(max_length=32)
    duration_minutes = models.PositiveIntegerField()

    class Meta:
        db_table = 'workouts'


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=80)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    activity_date = models.DateField()

    class Meta:
        db_table = 'activities'


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_rows')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_rows')
    score = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'leaderboard'
        unique_together = ('user', 'team')
