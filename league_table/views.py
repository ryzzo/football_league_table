from django.shortcuts import render, redirect
from .models import ClubStat, MatchStat
from .forms import MatchStatForm
from django.views.decorators.http import require_POST
from django.contrib import messages

def statsTable(request):
    stats = ClubStat.objects.all()
    return render(request, 'league_table/table/league_table.html', {'stats':stats})

def enterStat(request):
    if request.method == "POST":
        stats_form = MatchStatForm(request.POST)
        if stats_form.is_valid():

            stats_form.save()
            messages.success(request, ('Successfully added'))
            # retrive data from MatchStat model
            matchStat_obj = MatchStat.objects.last()
            home_team = getattr(matchStat_obj, 'home_team')
            away_team = getattr(matchStat_obj, 'away_team')
            home_goals = getattr(matchStat_obj, 'home_goals')
            away_goals = getattr(matchStat_obj, 'away_goals')

            # get ClubStat objects of the clubs
            home_team_stats = ClubStat.objects.get(club=home_team)
            away_team_stats = ClubStat.objects.get(club=away_team)

            # home team stats
            h_played = home_team_stats.played
            h_won = home_team_stats.won
            h_draw = home_team_stats.draw
            h_loss = home_team_stats.losses
            h_gd = home_team_stats.goal_dif
            h_points = home_team_stats.points

            # away team stats
            a_played = away_team_stats.played
            a_won = away_team_stats.won
            a_draw = away_team_stats.draw
            a_loss = away_team_stats.losses
            a_gd = away_team_stats.goal_dif
            a_points = away_team_stats.points

            home_team_stats.played = h_played + 1
            away_team_stats.played = a_played + 1
            match_goal_diff = abs(home_goals - away_goals)
            if home_goals > away_goals:
                home_team_stats.won = h_won + 1
                away_team_stats.losses = a_loss + 1
                home_team_stats.goal_dif = h_gd + match_goal_diff
                away_team_stats.goal_dif = a_gd - match_goal_diff
                home_team_stats.points = h_points + 3
                home_team_stats.save()
                away_team_stats.save()
            
            elif home_goals < away_goals:
                away_team_stats.won = a_won + 1
                home_team_stats.losses = h_loss + 1
                away_team_stats.goal_dif = a_gd + match_goal_diff
                home_team_stats.goal_dif = h_gd - match_goal_diff
                away_team_stats.points = a_points + 3
                home_team_stats.save()
                away_team_stats.save()

            else:
                home_team_stats.draw = h_draw + 1
                away_team_stats.draw = a_draw + 1
                home_team_stats.points = h_points + 1
                away_team_stats.points = a_points + 1
                home_team_stats.save()
                away_team_stats.save()
                


        else:
            messages.error(request, 'Error saving form')

       



        return redirect('league_table:enter_stats')

    
    
    stats_form = MatchStatForm()

    return render(request=request, template_name="league_table/table/enter_stats.html", context={'stats_form':stats_form})

def updateStats(home_team, away_team, home_goals, away_goals):
    '''Function that takes in the values from the form and apdates the league table'''
    stats = ClubStat.objects.get(club)