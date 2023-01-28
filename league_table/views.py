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
        else:
            messages.error(request, 'Error saving form')

        return redirect('league_table:enter_stats')

        # add data to the other models
    
    stats_form = MatchStatForm()

    return render(request=request, template_name="league_table/table/enter_stats.html", context={'stats_form':stats_form})

def updateStats(home_team, away_team, home_goals, away_goals):
    '''Function that takes in the values from the form and apdates the league table'''
    stats = ClubStat.objects.get(club)