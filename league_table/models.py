from django.db import models

class Club(models.Model):
    club_name = models.CharField(max_length=100)
    # Add information about the club eg. coach and home stadium

    def __str__(self):
        return self.club_name


class ClubStat(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, db_constraint=False)
    played = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)
    draw = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    goal_dif = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return f"{self.club} : {self.points} points"


class MatchStat(models.Model):
    home_team = models.ForeignKey(Club, on_delete=models.RESTRICT, null=False, related_name='home_team')
    away_team = models.ForeignKey(Club, on_delete=models.RESTRICT, null=False, related_name='away_team')
    home_goals = models.PositiveIntegerField(default=0)
    away_goals = models.PositiveIntegerField(default=0)
    winner = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f" {self.home_goals}{self.home_team} - {self.away_team}{self.away_goals}"

