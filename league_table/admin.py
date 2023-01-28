from django.contrib import admin
from .models import Club, ClubStat, MatchStat

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['club_name']
    search_fields = ['club_name']


@admin.register(ClubStat)
class ClubStatAdmin(admin.ModelAdmin):
    list_display = ['club', 'played', 'won', 'draw', 'losses', 'goal_dif', 'points']
    search_fields = ['club']


@admin.register(MatchStat)
class MatchStatAdmin(admin.ModelAdmin):
    list_display = ['home_team', 'away_team', 'home_goals', 'away_goals']
    
