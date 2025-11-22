from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    week = models.IntegerField()
    def __str__(self):
        return f"{self.team} - Week {self.week}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return self.name
